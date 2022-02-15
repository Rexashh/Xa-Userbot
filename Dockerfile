FROM rexashh/xa-userbot:buster

RUN git clone -b master https://github.com/Rexashh/Xa-Userbot  /home/userbot/ \
    && chmod 777 /home/userbot \
    && mkdir /home/userbot/bin/

WORKDIR /home/userbot/

CMD [ "bash", "start" ]
