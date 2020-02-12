FROM python:alpine

EXPOSE 5000

WORKDIR app

RUN apk add --no-cache python3-dev openssl-dev libffi-dev gcc && pip3 install --upgrade pip 


COPY ./requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY * /app/

CMD python app.py