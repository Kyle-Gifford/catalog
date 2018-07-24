# Simple Catalog App

## IP Address

52.24.66.168

## SSH Port for reviewer access

2200

## Website URL

http://52.24.66.168.xip.io

## Server Setup

# Obtain a web server through AWS lightsail

Go to https://aws.amazon.com/lightsail/ and create an account if you don't already have one then create an ubuntu server instance

# Update and upgrade packages on server

Connect to server via ssh and update and upgrade packages with

```sudo apt-get update``` ```sudo apt-get upgrade```

# Set up a firewall using ufw

Restrict all incoming traffic then allow all outgoing traffic, then allow 2200/tcp, www and ntp connections.

Then run ```sudo ufw enable``` to start firewall.

# Install these dependencies:

sudo apt-get -qqy install python python-pip

sudo apt-get install apache2

sudo pip2 install --upgrade pip

sudo apt-get -qqy install make zip unzip postgresql

sudo pip3 install flask packaging oauth2client redis passlib flask-httpauth

sudo pip3 install sqlalchemy flask-sqlalchemy psycopg2 bleach requests

sudo pip2 install flask packaging oauth2client redis passlib flask-httpauth

sudo pip2 install sqlalchemy flask-sqlalchemy psycopg2 bleach requests

sudo wget http://download.redis.io/redis-stable.tar.gz

tar xvzf redis-stable.tar.gz

cd redis-stable

make

sudo make install

sudo pip install httpauth

sudo pip install --upgrade google-api-python-client

sudo pip install flask-dance[sqla]

# Clone repo into server

While ssh'd into server navigate to /var/www/html/
Clone this repo into web server while in /var/www/html/

# Set up a wsgi apache server

Set up wsgi server to serve /var/www/html/catalog/web/views.wsgi

## Using the App

Now open a browser and navigate to http://52.24.66.168.xip.io and have fun using the app!

## Resources Used

udacity.com  
google.com
