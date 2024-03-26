FROM arm64v8/alpine:3.7
COPY qemu-aarch64-static /usr/bin

WORKDIR /app
COPY *.py ./
COPY requirements.txt .

RUN apk add --no-cache python3 py3-pip && pip3 install -r requirements.txt

ENTRYPOINT python3 main.py
