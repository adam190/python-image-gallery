#!/usr/bin/bash

export IMAGE_GALLERY_SCRIPT_VERSION="1.1"
CONFIG_BUCKET="edu.au.cc.imagegallery-config"

#install packages
sudo yum -y update
sudo yum install -y python3 git postgresql postgresql-devel gcc python3-devel
sudo amazon-linux-extras install -y nginx1

#configure/install custom software
cd /home/ec2-user
sudo git clone https://github.com/adam190/python-image-gallery.git
sudo chown -R ec2-user:ec2-user python-image-gallery
sudo su ec2-user -l -c "cd ~/python-image-gallery && pip3 install -r requirements.txt --user"

aws s3 cp s3://{CONFIG_BUCKET}/nginx/nginx.conf /etc/nginx
aws s3 cp s3://{CONFIG_BUCKET}/nginx/defaultd/image_gallery.conf /etc/nginx/default.d


#start/enable services
sudo systemctl stop postfix
sudo systemctl disable postfix
sudo systemctl start nginx
sudo systemctl enable nginx

sudo ec2-user -l -c "cd ~/python-image-gallery && ./start" >/var/log/image_gallery.log 2>&1 &
