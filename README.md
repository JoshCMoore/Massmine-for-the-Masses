# Massmine-for-the-Masses
A web application that allows a user to create queries for Twitter data in a simple, easily understandable user interface. The data will also be presented in a simple user interface to allow for basic analysis without the user ever having to directly interact with it.

To build from source, take a look at the webappInstallation.txt file.
 
Note to all users: This project is very much a work in progress. Please take precautions when installing on live systems. As this repository will not be maintained or updated after May 2019, it is advised that to fork your own branch of the project to edit and update as desired. Additionally, this project is NOT intended to be run on an external or unprotected network, as the default server employed by this project does not employ SSL or TLS for its web pages. 

DIY steps: To have full implementation of the forgot password functionality, you need to either set up an SMTP server or use a third party service and change from the current file-based system to an email-based system in webapp/webappproject/settings.py

# Documentation Report (Last updated Apr. 9, 2019)
https://docs.google.com/document/d/1AWmd1aNhKdGEgJwtUmRVg8DjnDtYorHeFS1gr_bBCEg/edit?usp=sharing

# Slides 
https://docs.google.com/presentation/d/1uO9E6uzCMvY16zW5k5j3LiHBbEx0g-w2cCiQJSXQaLY/edit?usp=sharing

# Roles and Subsystems.
Patricia Tanzer: Jelly Bean Counter - Keeping track of what we have and where we're at. Managing User Account subsystem.

Josh Moore: Meme Finder - Looking for problems in what we've written. Managing Massmine Integration and Dockerization ubsystem.

Logan Hornbuckle: Expert in Fingerpainting - Putting ideas into practice. Managing Query subsystem.

Morgan McIntyre: Professional Googler - Research and communication. Managing Analysis subsystem.

