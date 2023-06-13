FROM python:slim-buster

WORKDIR /app

ENV VIRTUAL_ENV=env_model
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . .
RUN pip install -Ur requirements.txt
ENV PORT=8000  
EXPOSE 8000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]