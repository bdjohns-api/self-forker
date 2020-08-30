FROM python:3.8.5

COPY src/ /app
WORKDIR /app

RUN pip3 install pipenv && pipenv install

ENTRYPOINT ["pipenv", "run", "python", "run.py"]

