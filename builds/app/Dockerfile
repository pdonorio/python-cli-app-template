ARG PYTHON_VERSION=3.8
FROM python:${PYTHON_VERSION}-alpine
# ARG ARGUMENT_TO_ENV=some_value
# ENV ARGUMENT_TO_ENV ${ARGUMENT_TO_ENV}

WORKDIR /tmp
COPY requirements.txt .
# RUN apk add --update --no-cache --virtual .build-deps \
#     libffi-dev openssl-dev python3-dev g++ make \
#     && pip --no-cache-dir install -r requirements.txt \
#     && apk del .build-deps
RUN pip --no-cache-dir install -r requirements.txt

RUN apk add --no-cache zsh
SHELL [ "/bin/zsh" ]
WORKDIR /
CMD [ "sleep", "infinity" ]
