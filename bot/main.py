from datetime import datetime
import pytz
from dotenv import load_dotenv

from football_api import get_fixture
from twitter import tweet_countdown, tweet_no_match, tweet_today
from os import environ as env

load_dotenv()

ARGENTINA_ID = 26
RIVER_ID = 435
BA_TZ = pytz.timezone("America/Argentina/Buenos_Aires")


def time_to_utc(dt: datetime, timezone: str = "America/Argentina/Buenos_Aires") -> datetime:
    local = pytz.timezone(timezone)
    local_dt = local.localize(dt, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt


def utc_to_tz(dt: datetime, tz: str) -> datetime:
    return dt.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(tz))


def utc_to_ba_tz(dt: datetime) -> datetime:
    return dt.replace(tzinfo=pytz.utc).astimezone(BA_TZ)


def main(team_id: int, team_name: str):
    schedule = get_fixture(team_id)
    if schedule:
        next_match = schedule[0]  # first match is next match
        match_date = utc_to_ba_tz(datetime.strptime(next_match['fixture']['date'][:19], "%Y-%m-%dT%H:%M:%S"))
        away = next_match['teams']['away']['name']
        home = next_match['teams']['home']['name']
        league = next_match['league']['name']
        how_many_days = (match_date - datetime.now(tz=BA_TZ)).days
        if how_many_days > 0:
            tweet_countdown(how_many_days=how_many_days, team_name=team_name,
                            away=away, home=home, league=league, match_date=match_date)
        else:
            tweet_today(team_name=team_name, home=home, away=away, league=league,
                        match_date=match_date)
    else:
        tweet_no_match(team_name=team_name)


if __name__ == "__main__":

    if env['team'] == 'RIVER':
        team_id = RIVER_ID
        team_name = "River Plate"
    elif env['team'] == 'ARG':
        team_id = ARGENTINA_ID
        team_name = "La Scaloneta"
    else:
        raise Exception('team not supported!')
    main(team_id, team_name)
