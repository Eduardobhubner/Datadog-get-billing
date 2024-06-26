FROM python:3

WORKDIR /app

COPY . .

RUN pip install requests

CMD [ "python", "app/index.py" ]