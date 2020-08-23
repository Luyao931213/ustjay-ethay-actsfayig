import os

import requests
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)
template = "<a href={{ link }}>{{ link }}</a>"


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def get_pig_page(phrase):
    url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    payload = {"input_text": phrase}
    response = requests.post(url, data=payload, allow_redirects=False)
    return response.headers.get('Location')


@app.route('/')
def home():
    fact = get_fact().strip()
    return get_pig_page(fact)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

