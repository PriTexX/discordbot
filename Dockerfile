FROM python:3.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

ENV TOKEN token here
ENV HOST_URL localhost

CMD ["python", "main.py"]