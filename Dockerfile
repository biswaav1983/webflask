FROM python:3.8.3-alpine

RUN adduser -D  demouser
USER demouser

RUN pip install --upgrade pip

WORKDIR /code

COPY --chown=demouser:demouser requirements.txt .

RUN pip install --user -r requirements.txt

COPY --chown=demouser:demouser src .

CMD ["python", "app.py"]
