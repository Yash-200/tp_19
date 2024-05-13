FROM python:3.11.9-bookworm

COPY app.py /app/
COPY req.txt /app/

RUN pip install -r /app/req.txt

CMD [ "python3","/app/app.py" ]
