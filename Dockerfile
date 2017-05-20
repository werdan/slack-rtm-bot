FROM python:2.7-slim
WORKDIR /root/

RUN mkdir plugins
COPY plugins/*.py plugins/
COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS client_secret.json
# ENTRYPOINT stdbuf -oL python main.py 2>&1  >> /var/log/rtmbot.log
CMD ["python", "./main.py"]