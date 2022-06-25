FROM debian:latest

RUN apt-get update -y && apt-get install gcc-10 -y && apt-get install g++-10 -y && apt-get install -y python3-pip && apt-get install -y dieharder

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ] 

CMD ["main.py"]