FROM python:3.11.9-bookworm

COPY app.py /app/
COPY req.txt /app/

RUN pip install -r /app/req.txt

CMD [ "streamlit","run","/app/app.py","--server.port","8000" ]
