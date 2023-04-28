FROM python:3.11.3
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY  app  /app/
COPY app_entrypoint.sh /app
CMD [ "./app_entrypoint.sh" ]
