FROM vckyouuu/geezprojects:buster

RUN git clone -b master https://github.com/SendiAp/Rose-Userbot  /home/userbot/ \
    && chmod 777 /home/userbot \
    && mkdir /home/userbot/bin/

WORKDIR /home/userbot/

CMD [ "bash", "start" ]
