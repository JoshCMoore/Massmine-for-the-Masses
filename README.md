# Massmine-for-the-Masses
A web application that allows a user to create queries for Twitter data in a simple, easily understandable user interface. The data will also be presented in a simple user interface to allow for basic analysis without the user ever having to directly interact with it.

To build from source, take a look at the webappInstallation.txt file.
 
Note to all users: This project is intended as a proof of concept only. Please take precautions when installing on live systems. As this repository will not be maintained or updated after May 2019, it is advised that to fork your own branch of the project to edit and update as desired. Additionally, this project is NOT intended to be run on an external or unprotected network, as the default server employed by this project does not employ SSL or TLS for its web pages. 

DIY steps: To have full implementation of the forgot password functionality, you need to either set up an SMTP server or use a third party service and change from the current file-based system to an email-based system in webapp/webappproject/settings.py

This specific project will not be maintained after the time of this posting (April 26, 2019). However, there is a fork planned to improve and further develop this project. Stay tuned!

# Roles and Subsystems.
Patricia Tanzer: Jelly Bean Counter - Keeping track of what we have and where we're at. Managing User Account subsystem.

Josh Moore: Meme Finder - Looking for problems in what we've written. Managing Studies, Massmine Integration, and Dockerization subsystem.

Logan Hornbuckle: Expert in Fingerpainting - Putting ideas into practice. Managing Query subsystem.

Morgan McIntyre: Professional Googler - Research and communication. Managing Analysis subsystem.

