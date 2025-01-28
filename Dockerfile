FROM python:3.11-alpine

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apk add ca-certificates
RUN pip3 install -r /app/requirements.txt

COPY . /app/

EXPOSE 8000

CMD [ "uvicorn", "src.main:app", "--workers", "1", "--host", "0.0.0.0", "--port", "8000" ]