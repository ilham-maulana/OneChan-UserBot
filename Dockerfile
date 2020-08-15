FROM movecrew/one4ubot:alpine-latest

RUN mkdir /OneChan-UserBot && chmod 777 /OneChan-UserBot
ENV PATH="/OneChan-UserBot/bin:$PATH"
WORKDIR /OneChan-UserBot

RUN git clone https://github.com/Ilham94/OneChan-UserBot -b sql-extended /OneChan-UserBot

#
# Copies session and config(if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /OneChan-UserBot/

#
# Finalization
#
CMD ["python3","-m","userbot"]
