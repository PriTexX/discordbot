FROM python:3.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --co-cache-dir -r requirements.txt

CMD ["python", "main.py"]