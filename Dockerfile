FROM greycilik/cilikuserbot:buster

RUN git clone -b Xa-Userbot https://github.com/Rexashh/Xa-Userbot /home/xauserbot/ \
    && chmod 777 /home/xauserbot \
    && mkdir /home/xauserbot/bin/

COPY ./sample_config.env ./config.env* /home/xauserbot/

WORKDIR /home/xauserbot/

CMD ["python3", "-m", "userbot"]
