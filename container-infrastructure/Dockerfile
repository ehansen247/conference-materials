FROM ubuntu:16.04
RUN apt-get update \
    && apt-get install -y python-pip \
    && apt-get install -y git
WORKDIR /myapp
ADD app.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD python app.py
EXPOSE 5000