
FROM python:3.9

# curl y dockerize
RUN apt-get update && apt-get install -y curl
RUN curl -sSL https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz | tar -C /usr/local/bin -xzv


WORKDIR /code

#requirements
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app

EXPOSE 8000

CMD ["dockerize", "-wait", "tcp://db:5432", "-timeout", "20s", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]