FROM python:3.8-slim-buster
USER root
RUN useradd -m train; \
    apt-get update && apt-get -y upgrade
USER train
WORKDIR /home/train/opt/code
COPY opt/code/requirements.txt .
RUN pip install -r requirements.txt
# add installed packages to PATH 
ENV PATH=/home/train/.local/bin:$PATH
COPY opt/ /home/train/opt/
# switch back to root and change ownership of the /home/train/opt directory since
# using chown while user is set to train outptus a permission denied error
USER root
RUN chown -R train /home/train/opt
# switch back to train in order to run the commands below
USER train
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "wsgi:app"]