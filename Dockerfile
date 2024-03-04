FROM python:3.10-slim

WORKDIR /app
COPY ./main.py /app/main.py
RUN pip install fastapi uvicorn pillow

ENV PORT 8080
EXPOSE $PORT
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
