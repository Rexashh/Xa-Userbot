FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
RUN git clone -b Xa-Userbot https://github.com/Rexashh/Xa-Userbot /home/Xa-Userbot/ \
    && chmod 777 /home/Xa-Userbot \
    && mkdir /home/Xa-Userbot/bin/
WORKDIR /home/Xa-Userbot/
COPY ./sample_config.env ./config.env* /home/Xa-Userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
