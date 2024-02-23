from openai import OpenAI
from trulens_eval import Feedback
from trulens_eval.feedback import GroundTruthAgreement
from trulens_eval.tru_custom_app import instrument
from trulens_eval import Tru

tru = Tru()
oai_client = OpenAI()

usertext = "Länder und Nationalitäten\nJeden Donnerstag treffen sich die Schüler in der Wohnung von Bärbel Kästner in Berlin. Bärbel ist Deutschlehrerin und unterrichtet heute eine Gruppe von sechs Personen. Jack kommt aus den Vereinigten Staaten von Amerika und studiert in San Diego. Er macht gerade ein Auslandssemester in Berlin. Neben ihm sitzt Pawel aus Polen. Er besitzt eine Autowerkstatt in der Nähe der polnischen Stadt Stettin. An Donnerstagen fährt er mit dem Zug nach Berlin, um am Kurs teilzunehmen. Er hat seinen besten Freund, den Briten William, in Deutschland kennengelernt. William lernt seit drei Jahren Deutsch bei Bärbel Kästner und liest gerne deutsche Bücher. Der Italiener Luigi hat Italien vor einigen Jahren verlassen. Er ist Koch und arbeitet in einem italienischen Restaurant in Berlin-Mitte. Luigi möchte seine Deutschkenntnisse verbessern. Glücklicherweise kann er sich mit Carla gut unterhalten. Sie ist Schweizerin und Italienisch ist ihre Muttersprache. Deutsch ist, wie auch Italienisch, eine der Amtssprachen in der Schweiz. Deswegen will Carla ein gutes Sprachniveau erreichen. Zu guter Letzt gibt es noch Jean-Pierre aus Paris. In Frankreich hat er vor dreißig Jahren seine österreichische Ehefrau kennengelernt. Vor drei Monaten sind sie zusammen nach Berlin gezogen, weil Jean-Pierre dort einen Job bei einer französischen Zeitung gefunden hat. Es gefällt ihnen inzwischen sehr gut in Deutschland."

class APP:
    @instrument
    def completion(self, prompt):
        completion = oai_client.chat.completions.create(
                model="gpt-4-0125-preview",
                temperature=0,
                messages=
                [
                    {"role": "user",
                    "content": f"basierend auf den folgenden Text, erzeuge 5 Fragen mit jeweils 3 falschen und einer richtigen Antwort, um zu prüfen, ob der Leser den Text versteht: {usertext}"
                    }
                ]
                ).choices[0].message.content
        return completion
    
llm_app = APP()

golden_set = [
    {"query": "Wo findet der Deutschkurs statt?", "response": "In der Wohnung von Bärbel Kästner"},
    {"query": "Aus welchem Land kommt Jack?", "response": "Aus den Vereinigten Staaten von Amerika"}
]

f_groundtruth = Feedback(GroundTruthAgreement(golden_set).agreement_measure, name = "Ground Truth").on_input_output()
# add trulens as a context manager for llm_app
from trulens_eval import TruCustomApp
tru_app = TruCustomApp(llm_app, app_id = 'Easyfox', feedbacks = [f_groundtruth])
# Instrumented query engine can operate as a context manager:
with tru_app as recording:
    llm_app.completion("Wo findet der Deutschkurs statt?")
    llm_app.completion("Aus welchem Land kommt Jack?")
    