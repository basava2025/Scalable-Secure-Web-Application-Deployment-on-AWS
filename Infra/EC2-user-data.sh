#!/bin/bash
yum update -y
yum install python3 -y
pip3 install flask pymysql

# Copy your app code to /home/ec2-user/app and run it
cd /home/ec2-user
git clone https://github.com/<your-username>/<your-repo>.git app
cd app/backend

python3 app.py &
