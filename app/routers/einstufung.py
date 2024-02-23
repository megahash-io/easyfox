
from fastapi import Request, APIRouter, WebSocket, Form
from app.config import Settings
from jinja2_fragments.fastapi import Jinja2Blocks
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_aiter import AsyncIteratorCallbackHandler
from langchain.schema import HumanMessage, SystemMessage
import asyncio, json

settings = Settings()
templates = Jinja2Blocks(directory=settings.TEMPLATE_DIR)

router = APIRouter()

@router.get("/einstufung")
def get_einstufung(request: Request):
    """Einstufungstest - lass dein Sprachniveau von der KI einstufen."""
    return templates.TemplateResponse( "einstufung.html", { "request": request } )

@router.post("/questions")
async def get_questions(request: Request):
    """Returns a list of questions based on the passed text"""
    print("Generating questions...")
    ajson = json.loads(await request.body())
    usertext = ajson['usertext']

    chat = ChatOpenAI(model_name='gpt-4-0125-preview', temperature=0)
    messages = [
        SystemMessage(
            content="You are a helpful assistant"
        ),
        HumanMessage(
            content=f"basierend auf den folgenden Text, erzeuge 5 Fragen mit jeweils 3 falschen und einer richtigen Antwort, um zu prüfen, ob der Leser den Text versteht: {usertext}"
        ),
    ]
    questions = chat(messages)
    print("questions ready, generating json...", )
    messages = [
        SystemMessage(
            content="You are a helpful assistant that generates JSON from text"
        ),
        HumanMessage(
            content=f"Konvertiere den folgenden Text in ein strukturiertes JSON-Format. Benenne die Schlüssel auf Deutsch: {questions.content}"
        ),
    ]
    r = chat(messages).content
    r = r.replace("\n    ","")
    r = r.replace("```json\n","")
    r = r.replace("\n```","")
    r = r.replace("\n","")

    json_questions = json.loads(r)
    print(json_questions)
    return templates.TemplateResponse( "questions.html", { "request": request, "questions": json_questions['Fragen'] } )

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    load_dotenv()
    handler = AsyncIteratorCallbackHandler()
    model = ChatOpenAI(streaming=True, callbacks=[handler], model_name='gpt-4-0125-preview', temperature=0)

    template = """
        <div hx-swap-oob="beforeend:#einstufung_results_raw">{token}</div>
    """

    end_template = """
        <div hx-swap-oob="beforeend:#einstufung_results_raw"><div _="init show #clear_btn"></div></div>
    """
    
    while True:
        data = await websocket.receive_json()
        message = data['usertext']
        response=''
        prompt = f"""Du bist ein Experte für Deutsch als Fremdsprache. 
                    Analysiere den folgenden Text und bestimme welchem Sprachniveau es entspricht. 
                    Begründe deine Entscheidung und antworte auf Deutsch. Erkläre 
                    anhand von Beispielen aus dem Text, wie die Abgrenzung zur jeweils niedrigeren 
                    Niveaustufe ist: {message}"""
        
        task = asyncio.create_task(model.agenerate(messages=[[HumanMessage(content=prompt)]]))
        
        async for token in handler.aiter():
            response = response + token 
            await websocket.send_text(template.format(token=token))

        await task
        await websocket.send_text(end_template)
        handler.done()
    
