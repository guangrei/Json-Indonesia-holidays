FROM alpine:latest

RUN apk add --update --no-cache jq git python3 py3-pip

RUN pip install -r requirements.txt

COPY entrypoint /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint"]