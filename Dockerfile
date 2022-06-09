FROM Rexashh/Xa-Userbot:buster

RUN git clone -b Xa-Userbot https://github.com/Rexashh/Xa-Userbot /home/userbot/ \
    && chmod 777 /home/userbot \
    && mkdir /home/userbot/bin/

COPY ./sample_config.env ./config.env* /home/userbot/

WORKDIR /home/userbot/

CMD ["bash","start"]
