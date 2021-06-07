FROM jupyter/scipy-notebook
USER root
COPY opt/ /opt/
WORKDIR /opt/ml/code
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["deploy"]
