FROM ubuntu:latest

RUN apt-get update && apt-get install -y \ 
    software-properties-common sudo tmux vim wget curl lsof psmisc tzdat

WORKDIR /usr/local/geofox
COPY . /usr/local/geofox

RUN yes | ./bin/deps.sh
RUN yes | ./bin/venv.sh

CMD ["./bin/spawn.sh"]