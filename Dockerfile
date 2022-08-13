FROM python:3.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

ENV TOKEN OTg5OTMwNjYwNzc0OTUyOTkx.GEepAS.99ejrEw0DUsGnLf9N0T6mWtyAlKHMG4uC_0nks
ENV HOST_URL localhost

CMD ["python", "main.py"]