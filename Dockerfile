FROM alpine:latest

RUN apk add --no-cache python3-dev 
RUN apk add py3-pip && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3  --no-cache-dir install flask

EXPOSE 5000

ENTRYPOINT [ "python3" ]
CMD [ "SubwayAPI.py" ]