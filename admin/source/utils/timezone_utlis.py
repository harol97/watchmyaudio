from datetime import datetime

import pytz


def to_utc(from_datetime: datetime, from_timezone: str) -> datetime:
    local = pytz.timezone(from_timezone)
    local_dt = local.localize(from_datetime, is_dst=None)
    return local_dt.astimezone(pytz.utc)


def to_timezone(from_datetime_utc: datetime, to_timezone: str) -> datetime:
    specific_timezone = pytz.timezone(to_timezone)
    return from_datetime_utc.astimezone(specific_timezone)
