from multiprocessing import cpu_count

worker_class = "uvicorn.workers.UvicornWorker"
bind = "0.0.0.0:80"
# workers = (2 * cpu_count()) + 1
timeout = 30
