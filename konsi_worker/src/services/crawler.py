from typing import Dict, Any
import requests
import json


def get_data(username: str, password: str) -> Dict[str, Any]:

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'http://ionic-application.s3-website-sa-east-1.amazonaws.com',
        'Referer': 'http://ionic-application.s3-website-sa-east-1.amazonaws.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
    }

    json_data = {
        'login': 'testekonsi',
        'senha': 'testekonsi',
    }

    response = requests.post(
        'http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/login',
        headers=headers,
        json=json_data,
        verify=False,
    )

    response = requests.get(
        'http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/offline/listagem/074.687.335-20',
        headers=response.headers,
        verify=False,
    )

    return


if __name__ == '__main__':
    get_data(None, None)
