import os
from datetime import datetime
from random import choice
from typing import Any, Dict
import json
from os import environ as env

from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session

load_dotenv()

twitter_session = OAuth1Session(env["API_KEY"], env["API_KEY_SECRET"], env["ACCESS_TOKEN"], env["ACCESS_TOKEN_SECRET"])

template_tweet_countdown = """
¡Faltan {how_many_days} días para que juegue {team_name}! 🇦🇷

⚽️ Próximo partido:
{match_date} - {home} vs. {away}
🏆 {league}
"""

template_tweet_today = """
¡¡Es hoy!! ¡Hoy juega {team_name}!
🔥🔥🔥🔥
{match_date}hs - {home} vs. {away}
{league}
"""

template_no_match_tweet = """
Todavía no hay fechas agendadas para {team_name} 😢
"""


def __upload_random_image(images_dir: str) -> str:
    complete_img_dir = f'pics/{images_dir}'
    filename = choice(os.listdir(complete_img_dir))
    url_media = 'https://upload.twitter.com/1.1/media/upload.json'
    with open(f"{complete_img_dir}/{filename}", 'rb') as f:
        files = {"media": f}
        response = twitter_session.post(url_media, files=files)

    if response.status_code != 200:
        raise Exception(f"Uploading picture fails: {response.text}")
    return json.loads(response.text)['media_id']


def __tweet(message: str, img_dir: str) -> Dict[str, Any]:
    media_id = __upload_random_image(img_dir)
    url_text = 'https://api.twitter.com/1.1/statuses/update.json'
    response = twitter_session.post(url_text, params={'status': message, "media_ids": [media_id]})
    if response.status_code != 200:
        raise Exception(f"Uploading text fails: {response.text}")
    return json.loads(response.content)


def tweet_countdown(team_name: str, home: str, away: str, how_many_days: int, league: str,
                    match_date: datetime) -> Dict[str, Any]:
    return __tweet(template_tweet_countdown.format(how_many_days=how_many_days, team_name=team_name,
                                                   away=away, home=home, league=league,
                                                   match_date=match_date.strftime('%d/%m')), img_dir='match')


def tweet_today(team_name: str, home: str, away: str, league: str,
                match_date: datetime) -> Dict[str, Any]:
    return __tweet(template_tweet_today.format(team_name=team_name,
                                               away=away, home=home, league=league,
                                               match_date=match_date.strftime('%H:%M')), img_dir='today')


def tweet_no_match(team_name: str) -> Dict[str, Any]:
    return __tweet(template_no_match_tweet.format(team_name=team_name), img_dir='no_match')


