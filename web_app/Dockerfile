# docs: https://hub.docker.com/_/python
FROM python:3

ENV SECRET_KEY=dev

WORKDIR /web_app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]