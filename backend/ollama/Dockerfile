FROM ollama/ollama

COPY ./pull-model.sh /tmp/pull-model.sh

WORKDIR /tmp

RUN chmod +x pull-model.sh \
    && ./pull-model.sh

EXPOSE 11434