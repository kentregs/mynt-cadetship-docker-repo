FROM tensorflow/tensorflow
USER root
RUN useradd --create-home train; \
    apt-get update && apt-get -y upgrade
WORKDIR /home/train
COPY opt/code/requirements.txt .
RUN pip freeze > requirements.txt
USER train
COPY opt/ /opt/
