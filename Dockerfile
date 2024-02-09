FROM alpine:3.19

RUN apk --update --no-cache add py3-pip \
 && pip install --no-cache-dir flask --break-system-packages \
 && mkdir /godutch

COPY src/ /godutch

EXPOSE 8080

WORKDIR /godutch
ENTRYPOINT [ "python3", "main.py" ]
