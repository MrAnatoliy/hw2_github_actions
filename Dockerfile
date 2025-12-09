FROM python:3.12-slim-bullseye

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./src ./src
COPY ./pyproject.toml ./

RUN pip install -e .

ENV PYTHONPATH=/app/src:$PYTHONPATH

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
EXPOSE 8080