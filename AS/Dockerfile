FROM --platform=linux/amd64 python:3.8-slim-buster as build

RUN apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN groupadd -g 799 nyu && \
    useradd -r -u 999 -g nyu nyu
    
# Set up a working folder and install the pre-reqs
WORKDIR /app

USER nyu

COPY --chown=nyu:nyu . .

CMD [ "python", "./run.py" ]
