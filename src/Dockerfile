From ubuntu:18.04

RUN apt-get update -y
RUN apt install python3 -y&& apt install python3-pip -y&& pip3 install django==2.1.7&&pip3 install numpy==1.16.2&&pip3 install matplotlib==3.0.3 

RUN apt install wget -y&&apt install unzip -y&&wget http://www.massmine.org/downloads/massmine-1.1.0-linux-x86_64.zip&& unzip massmine-1.1.0-linux-x86_64.zip&&ln -s `pwd`/massmine /usr/local/bin

RUN apt install git -y

RUN wget http://www.nicholasvanhorn.com/software/jsan-1.3.0-OSX-10.10.tar.gz&&tar -xzf jsan-1.3.0-OSX-10.10.tar.gz&&ln -s `pwd`/jsan/jsan /usr/local/bin

#RUN git clone https://github.com/JoshCMoore/Massmine-for-the-Masses.git

# Replace USERNAME and PASSWORD with your account info
 RUN git clone https://USERNAME:PASSWORD@github.com/JoshCMoore/Massmine-for-the-Masses.git

# This is where we should copy our source files
COPY ./Massmine-for-the-Masses/src/webapp /

Expose 8000

# This should either start the server or run a startup script
CMD python3 /manage.py runserver 0.0.0.0:8000
