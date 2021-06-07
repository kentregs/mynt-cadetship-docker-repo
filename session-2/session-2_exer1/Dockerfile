FROM jupyter/scipy-notebook
USER root
WORKDIR /opt/ml/code
COPY opt/ml/code/requirements.txt .
RUN pip install -r requirements.txt
COPY opt/ /opt/
ENTRYPOINT [ "python3"]
CMD ["deploy"]
