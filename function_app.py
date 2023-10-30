import logging
import azure.functions as func
import requests
from bs4 import BeautifulSoup

def check_line_text(req: func.HttpRequest, timerInfo: func.TimerRequest):
    url = "https://azrstage.simplifiedlogistics.com/heartbeattest/heartBeatReport.aspx"
    text_object = "HeartBeat Status Good"

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        contein = soup.get_text()

        if text_object in contein:
            return f"The Line '{text_object}' Was found Successfully in the page."
        else:
            return f"The Line '{text_object}' Was Not found in the page."
    else:
        return f"The web page could not be accessed. Status code: {response.status_code}"
