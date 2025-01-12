from datetime import datetime
from uuid import uuid4

from apscheduler.job import Job
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler


class Scheduler:
    obj: "Scheduler | None" = None

    def __init__(self) -> None:
        jobstores = {"default": SQLAlchemyJobStore(url="sqlite:///database2.db")}
        self.apscheduler = BackgroundScheduler(jobstores=jobstores)

    @classmethod
    def get_instance(cls) -> "Scheduler":
        if not cls.obj:
            cls.obj = Scheduler()
        return cls.obj

    def append_job(self, func, start_date: datetime, *func_params) -> Job:
        new_job = self.apscheduler.add_job(
            func, "date", run_date=start_date, args=func_params, id=str(uuid4())
        )
        return new_job
