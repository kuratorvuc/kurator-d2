import requests

from fastapi import FastAPI
from fastapi.responses import FileResponse
from bs4 import BeautifulSoup  # для парсера страницы

app = FastAPI()


def parse_html_to_dict(html_content):
    #TODO сделать парсер страницы сгенерированной с устройства D1
    #HTML страница выглядит так:
    '''
    <!DOCTYPE HTML>
    <html>
    <script type="text/javascript" src="/FD126C42-EBFA-4E12-B309-BB3FDD723AC1/main.js?attr=cNXeajFiwuUUA6mQ86Jvf2mprHCLhZ_VDvAvhxKXReTO3UyzIhh_9hu7GJ1ZWuNN" charset="UTF-8"></script>
    <h1>Test serv</h1>
    Temp: 26.97 °C<br>
    Pressure: 99023.97<br>
    altitude: 193.36<br>
    </html>
    '''
    return html_content


@app.get("/")
def index():
    return FileResponse('static/index.html')


@app.get("/data")
def get_data():
    response = requests.get('http://192.168.0.108')  # на этоп IP поднимается сервер устройства D1

    # parsed_data = parse_html_to_dict(response.text)
    # return parsed_data

    data = {
        'temp': '36',
        'pressure': '180',
        'altitude': '20'
    }
    return data
