# Dockerfile

FROM python:3

ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --upgrade pip

RUN pip install pandas 
    
#  or install packages from the requirements.txt file (must be in same dir as Dockerfile)
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt