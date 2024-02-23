FROM megahashio/easyfox:latest

WORKDIR /app

COPY . .

RUN npm i

EXPOSE 3999

RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

CMD . /opt/venv/bin/activate && exec uvicorn app.main:app --host 0.0.0.0 --port 3999

