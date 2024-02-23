<h1 align="center">Easyfox</h1>
<h2 align="center">Featuring OpenAI, FastAPI, TruLens, HTMX and TailwindCSS</h2>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![GitHub Issues](https://img.shields.io/github/issues/megahash-io/easyfox)
![Github Pull Requests](https://img.shields.io/github/issues-pr/megahash-io/easyfox)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> AI based german language learning app. Have your german text analyzed and classified by GER level. Additionally, let the AI generate practice tasks.
    <br>
</p>
<p align="center">
  <a href="" rel="noopener">
 <img width=600px height=400px src="https://github.com/megahash-io/easyfox/blob/main/demo.gif" alt="Project demo"></a>
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [🏁 Getting Started ](#-getting-started-)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
    - [Using Codespaces](#using-codespaces)
    - [Locally](#locally)
- [🔧 Running the tests ](#-running-the-tests-)
- [🎈 Test Data ](#-testdata-)
  - [:sparkles:Build a Python-Backed Frontend With HTMX and TailwindCSS:sparkles:](#sparklesbuild-a-python-backed-frontend-with-htmx-and-tailwindcsssparkles)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Authors ](#️-authors-)
- [🎉 Acknowledgements ](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

easyfox was born to provide AI based german language training and learning tools.

## 🏁 Getting Started <a name = "getting_started"></a>

Follow the instructions below to get easyfox up and running locally.

### Prerequisites

The example app was created with **Python 3.11**, but it is likely compatible with earlier versions. However, I would highly recommend using the latest version of Python. The rest of the dependencies are listed in the `requirements.txt` file.

```
pydantic
langchain
openai
fastapi[all]
jinja2
jinja2-fragments
python-multipart
pytest
pytailwindcss
tinydb
markdown
python-multipart
trulens_eval 
chromadb
```

The `fastapi[all]` dependency installs some other optional dependencies and features. It also includes `uvicorn`, which is used as the server to run your code. (You could choose to just use `fastapi` and `uvicorn[standard]` separately, if you prefer.)

> Why is there a `pyproject.toml` file? If you use a package manager (i.e., I use `pdm`), you can use your package manager to install dependencies. Otherwise, you can go the more traditional route using the `requirements.txt` file. If you use Codespaces, you won't need to worry about dependencies!

### Installing

#### Using Codespaces
Press the `<> Code` button above and select `Create a Codespace on main`. This will open a new window in your browser, where you can run the code in a virtual environment.

https://user-images.githubusercontent.com/8632637/228152014-a73297f5-dfd7-400c-96b1-17239dcdb633.mp4

#### Locally
Create a copy of the repo using the `Use this template` button above. Select `Create a new repository`.

> **Warning**
> Be sure to select **`Include all branches`** when cloning the repo.

After cloning or using this template, you will need to create a virtual environment. Navigate to the location where you have cloned the project (your project root) and run the following command in your terminal:

```
python -m venv .venv
```

This will create a `.venv` directory within your project.

Next, activate your environment:

```
# On Windows
.\.venv\Scripts\activate

# On MacOS/Linux
$ source .venv/bin/activate
```

Then, install the requirements:

```
python -m pip install -r requirements.txt
```

## 🔧 Running the tests <a name = "tests"></a>

After activating your virtual environment, you can run tests by typing `pytest` on the command line. This makes sure that your application runs and can generate a "Hello World" message.

```
pytest
```

If everything has gone well so far, all tests should pass.


## 🎈 Test Data <a name="testdata"></a>

You will need some german texts to test the app with. Here are some, together with the approximate GER classification level:

### A2 Level

```text
Meine gemütliche Wohnung
Ich wohne in Bogor, Indonesien, in der Nähe von der Hauptstadt. Ich habe eine große Wohnung. Meine Wohnung hat zwei Etagen. Im Erdgeschoss gibt es ein Schlafzimmer, eine große Küche, ein Esszimmer, ein Wohnzimmer, ein leeres Zimmer, zwei Badezimmer, zwei Garagen und einen Garten.

Ich habe eine große Küche, weil meine Mutter gern kocht und backt. In der Küche gibt es drei Kühlschränke, einen Ofen, ein Waschbecken, einen Herd und einen Tisch. Im Esszimmer steht ein großer Esstisch mit 6 Stühlen. Im Wohnzimmer habe ich ein Sofa, einen Tisch und einen Fernseher. Mein Wohnzimmer ist nicht hell, aber sehr gemütlich. Ich sitze gern hier, weil das mein Lieblingszimmer ist. Die Schlafzimmer von meiner Mutter und meinem Bruder sind auch im Erdgeschoss. Da gibt es ein Bett, einen Kleiderschrank, einen Arbeitstisch und einen Stuhl. Mein Bruder hat einen Computertisch in seinem Schlafzimmer. Er spielt gern Computer.

In der ersten Etage gibt es zwei Schlafzimmer, ein Badezimmer und einen Balkon. Mein Schlafzimmer befindet sich hier auf dieser Etage. Mein Schlafzimmer ist groß und hell. In meinem Schlafzimmer habe ich einen großen Kleiderschrank, ein Bett, einen Schreibtisch und einen Stuhl. Ich habe mein eigenes Badezimmer. Es ist sehr klein, aber sehr praktisch. Ich habe auch einen Balkon. Da lese ich manchmal Bücher. Draußen gibt es einen Garten. In meinem Garten habe ich ein paar Pflanzen und einen Fischteich. In meinem Fischteich gibt es viele Fische. Sie sind meine Lieblingstiere. In meiner Garage stehen ein Fahrrad und ein Auto. Neben der Garage gibt es einen kleinen Schuppen für die ungebrauchten Kisten. Ich mag meine Wohnung sehr und kann problemlos einige Tage zu bleiben.
```

```text
Länder und Nationalitäten
Jeden Donnerstag treffen sich die Schüler in der Wohnung von Bärbel Kästner in Berlin. Bärbel ist Deutschlehrerin und unterrichtet heute eine Gruppe von sechs Personen.

Jack kommt aus den Vereinigten Staaten von Amerika und studiert in San Diego. Er macht gerade ein Auslandssemester in Berlin.

Neben ihm sitzt Pawel aus Polen. Er besitzt eine Autowerkstatt in der Nähe der polnischen Stadt Stettin. An Donnerstagen fährt er mit dem Zug nach Berlin, um am Kurs teilzunehmen. Er hat seinen besten Freund, den Briten William, in Deutschland kennengelernt.

William lernt seit drei Jahren Deutsch bei Bärbel Kästner und liest gerne deutsche Bücher.

Der Italiener Luigi hat Italien vor einigen Jahren verlassen. Er ist Koch und arbeitet in einem italienischen Restaurant in Berlin-Mitte. Luigi möchte seine Deutschkenntnisse verbessern. Glücklicherweise kann er sich mit Carla gut unterhalten. Sie ist Schweizerin und Italienisch ist ihre Muttersprache. Deutsch ist, wie auch Italienisch, eine der Amtssprachen in der Schweiz. Deswegen will Carla ein gutes Sprachniveau erreichen.

Zu guter Letzt gibt es noch Jean-Pierre aus Paris. In Frankreich hat er vor dreißig Jahren seine österreichische Ehefrau kennengelernt. Vor drei Monaten sind sie zusammen nach Berlin gezogen, weil Jean-Pierre dort einen Job bei einer französischen Zeitung gefunden hat. Es gefällt ihnen inzwischen sehr gut in Deutschland.
```

## ⛏️ Built Using <a name = "built_using"></a>

- FastAPI
- Jinja2
- TailwindCSS
- OpenAI
- htmx
- TruLens
- ChromaDB

## ✍️ Authors <a name = "authors"></a>

- [@megahash-io](https://github.com/tataraba) - Ina Emmerich, Marcelo Emmerich
