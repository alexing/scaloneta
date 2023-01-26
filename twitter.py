from datetime import datetime
from typing import Optional

import pytwitter
from os import environ as env

from dotenv import load_dotenv

load_dotenv()

api = pytwitter.Api(
    consumer_key=env["API_KEY"],
    consumer_secret=env["API_KEY_SECRET"],
    access_token=env["ACCESS_TOKEN"],
    access_secret=env["ACCESS_TOKEN_SECRET"],
)

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


def __tweet(message: str) -> Optional[str]:
    posted_tweet = api.create_tweet(text=message)
    return posted_tweet.id


def tweet_countdown(team_name: str, home: str, away: str, how_many_days: int, league: str,
                    match_date: datetime) -> Optional[str]:
    return __tweet(template_tweet_countdown.format(how_many_days=how_many_days, team_name=team_name,
                                                   away=away, home=home, league=league,
                                                   match_date=match_date.strftime('%d/%m')))


def tweet_today(team_name: str, home: str, away: str, league: str,
                match_date: datetime) -> Optional[str]:
    return __tweet(template_tweet_today.format(team_name=team_name,
                                               away=away, home=home, league=league,
                                               match_date=match_date.strftime('%H:%M')))


def tweet_no_match(team_name: str) -> Optional[str]:
    return __tweet(template_no_match_tweet.format(team_name=team_name))
