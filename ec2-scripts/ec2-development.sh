#!/usr/bin/bash

#install packages
sudo yum -y update
sudo yum install -y nano tree python3
sudo yum install -y git

#config/install custom software
cd /home/ec2-user
git clone https://github.com/adam190/python-image-gallery.git
chown -R ec2-user:ec2-user python-image-gallery
su ec2-user -c "cd ~/python-image-gallery && pip3 install -r requirements.txt --user"


#start/enable services
sudo systemctl stop postfix
sudo systemctl diable postfix
