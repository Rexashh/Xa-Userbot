# Using Python Slim-Buster
FROM kyyex/kyy-userbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Xa-Userbot ━━━━━

RUN git clone -b Tonic-Userbot https://github.com/Rexashh/Xa-Userbot  /home/userbot/
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Tonic990/Tonic-Userbot/Tonic-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
