from datetime import datetime, timezone
from uuid import uuid4

from apscheduler.job import Job
from apscheduler.jobstores.base import JobLookupError
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler


class Scheduler:
    obj: "Scheduler | None" = None

    def __init__(self) -> None:
        jobstores = {"default": SQLAlchemyJobStore(url="sqlite:///database2.db")}
        self.apscheduler = BackgroundScheduler(jobstores=jobstores)
        self.jobs_to_finish_process: set[str] = set()

    @classmethod
    def get_instance(cls) -> "Scheduler":
        if not cls.obj:
            cls.obj = Scheduler()
        return cls.obj

    def append_job(self, func, start_date: datetime, *func_params) -> Job:
        job_id = str(uuid4())
        new_job = self.apscheduler.add_job(
            func, "date", run_date=start_date, args=[job_id, *func_params], id=job_id
        )
        return new_job

    def delete_job(self, job_id: str):
        try:
            self.jobs_to_finish_process.add(job_id)
            self.apscheduler.remove_job(job_id)
        except JobLookupError:
            ...

    def should_process_job_finish(self, job_id: str) -> bool:
        try:
            self.jobs_to_finish_process.remove(job_id)
            return True
        except:
            return False
