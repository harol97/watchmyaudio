# BACKEND WHATCHMYAUDIO

this project use python 3.11.

Use [uv Astral tool](https://docs.astral.sh/uv/getting-started/installation/). It detect python version automatically from .python-version file.

Please check instructions in next sections

## DEVELOP ENVIRONMENT

Execute next steps once:

    1. uv sync
    2. uv pip install librosa
    3. uv run python execute_seddings.py (execute only once)
    4. user administrator is (username:administrator@gmail.com, password:administrator)

Now when you want to start server execute:

    1. uv run fastapi dev

you can check [openapi documentation](http://localhost:8000/docs)
