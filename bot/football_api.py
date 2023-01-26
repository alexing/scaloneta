from typing import Any, Dict, List, Optional
import requests
import json
from os import environ as env

from dotenv import load_dotenv

load_dotenv()


def get_fixture(team_id: int) -> Optional[List[Dict[str, Any]]]:
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': env["FOOTBALL_TOKEN"]
    }
    url = f'https://v3.football.api-sports.io/fixtures?next=10&team={team_id}'

    response = requests.get(url, headers=headers)
    if response.status_code != requests.codes.ok:
        raise requests.exceptions.RequestException(f'response {response.status_code} -> {response.content}')
    response_content = json.loads(response.content)
    if response_content:
        return response_content['response']
    return None
