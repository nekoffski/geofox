FROM ubuntu:latest

RUN apt-get update && apt-get install -y \ 
    software-properties-common sudo tmux vim wget curl lsof psmisc
RUN add-apt-repository ppa:deadsnakes/ppa
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
RUN apt-get update

WORKDIR /usr/local/geofox
COPY . /usr/local/geofox

RUN yes | ./bin/deps.sh
RUN yes | ./bin/venv.sh

CMD ["./bin/spawn.sh"]