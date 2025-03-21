FROM arm64v8/alpine:3.21
COPY qemu-aarch64-static /usr/bin

WORKDIR /app
COPY *.py ./
COPY requirements.txt .

RUN apk add --no-cache python3 py3-pip
RUN pip3 install --break-system-packages -r requirements.txt

ENTRYPOINT python3 main.py
