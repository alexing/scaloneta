import os
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[0]

from football_api import get_fixture
from time_utils import BA_TZ, utc_to_ba_tz
from twitter import tweet_countdown, tweet_no_match, tweet_today

ARGENTINA_ID = 26
RIVER_ID = 435


def lambda_handler(event, context):
    if os.getenv('TEAM') == 'RIVER':
        team_id = RIVER_ID
        team_name = "River Plate"
    elif os.getenv('TEAM') == 'ARG':
        team_id = ARGENTINA_ID
        team_name = "La Scaloneta"
    else:
        raise Exception('team not supported!')

    schedule = get_fixture(team_id)
    if schedule:
        next_match = schedule[0]  # first match is next match
        match_date = utc_to_ba_tz(datetime.strptime(next_match['fixture']['date'][:19], "%Y-%m-%dT%H:%M:%S"))
        away = next_match['teams']['away']['name']
        home = next_match['teams']['home']['name']
        league = next_match['league']['name']
        how_many_days = (match_date - datetime.now(tz=BA_TZ)).days
        if how_many_days > 0:
            tweet = tweet_countdown(how_many_days=how_many_days, team_name=team_name,
                                    away=away, home=home, league=league, match_date=match_date)
        else:
            tweet = tweet_today(team_name=team_name, home=home, away=away, league=league, match_date=match_date)
        return {"statusCode": 200, "tweet": tweet['text']}
    else:
        if not datetime.now().day % 3:  # every 3 days
            tweet = tweet_no_match(team_name=team_name)
            return {"statusCode": 200, "tweet": tweet['text']}

    return {"statusCode": 404, "tweet": 'none'}
