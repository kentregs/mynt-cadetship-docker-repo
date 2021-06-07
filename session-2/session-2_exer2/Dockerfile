FROM jupyter/scipy-notebook
USER root
RUN useradd -m app; \ 
    apt-get update && apt-get -y upgrade
WORKDIR /home/app
COPY opt/ml/code/requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt
USER app
COPY opt/ .
ENTRYPOINT [ "python3"]
CMD ["deploy"]
