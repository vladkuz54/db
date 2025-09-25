FROM ubuntu:latest

WORKDIR /load_test

COPY load_test.sh .

RUN chmod +x load_test.sh \
    && apt-get update \
    && apt-get install -y wrk

CMD ["./load_test.sh"]