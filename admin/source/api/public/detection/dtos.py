from datetime import datetime

from source.utils.custom_base_model import CustomBaseModel


class Report(CustomBaseModel):
    client_name: str
    radio_station_name: str
    filename: str
    detection_date: datetime
