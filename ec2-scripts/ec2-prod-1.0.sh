#!/usr/bin/bash

export IMAGE_GALLERY_SCRIPT_VERSION="1.0"

#install packages
sudo yum -y update
sudo yum install -y python3 git

#configure/install custom software
cd /home/ec2-user
sudo git clone https://github.com/adam190/python-image-gallery.git
sudo chown -R ec2-user:ec2-user python-image-gallery
sudo su ec2-user -l -c "cd ~/python-image-gallery && pip3 install -r requirements.txt --user"

#start/enable services
sudo systemctl stop postfix
sudo systemctl disable postfix

sudo ec2-user -l -c "cd ~/python-image-gallery && ./start" >/var/log/image_gallery.log 2>&1 &
