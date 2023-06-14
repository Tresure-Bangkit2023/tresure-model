FROM python:slim-buster

WORKDIR /app

ENV VIRTUAL_ENV=env_model
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . .
RUN pip install -r requirements.txt
ENV PORT=8000  
EXPOSE 8000

CMD exec gunicorn --bind :$PORT --workers 2 --threads 8 --timeout 0 app:app
