FROM python:3.11.3
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY  app  /app/
CMD ["uvicorn", "app.main:server", "--host=0.0.0.0", "--reload"]
