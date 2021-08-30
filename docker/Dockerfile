FROM python:3.7.10-buster

# install pipenv
RUN pip install pipenv

RUN adduser model
RUN mkdir /app && \
    chown model:model /app
WORKDIR /app

# Copy local python code, scripts and pipenv
COPY Pipfile Pipfile.lock setup.py entrypoint.sh /app/
COPY src /app/src/

# Sync pipenv environment
RUN pipenv install --deploy --system

USER model

ENTRYPOINT ["/app/entrypoint.sh"]
