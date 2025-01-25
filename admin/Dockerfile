FROM  python:3.11

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
ADD https://astral.sh/uv/0.5.14/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

RUN apt install -y ffmpeg

WORKDIR /app

COPY uv.lock pyproject.toml ./
RUN uv sync --frozen --no-dev

COPY . .

RUN echo uv run python execute_seddings.py >> start.sh
RUN echo uv run gunicorn main:app >> start.sh

CMD ["sh", "start.sh"]
