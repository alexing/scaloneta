from datetime import datetime
import pytz

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
