FROM debian:buster
#FROM arm64v8/debian:latest

RUN apt-get update \
    && apt-get -y install python3 \
    python3-pyqt5

RUN pip3 install python-dotenv requests pillow

RUN mkdir /www
WORKDIR /www

#RUN pip3 install charlcd \
#    && pip3 install iot_message

ADD ./app /www/app/
ADD ./main.py /www/main.py

RUN ls -la
CMD [ "python3", "main.py" ]