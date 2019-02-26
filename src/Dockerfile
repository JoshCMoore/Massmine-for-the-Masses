From ubuntu:18.04

RUN apt-get update -y&& apt install python3 -y&& apt install python3-pip -y&& pip3 install django==2.1.7 

# This is where we should copy our source files
COPY ./Front-end /

Expose 80

# This should either start the server or run a startup script
CMD python3 /Front-end/manage.py runserver 


