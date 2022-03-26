#!/bin/bash -e
# update repo
sudo apt update -y
sudo apt upgrade -y
# install app
sudo apt install -y redis
# 创建pip配置文件
if [ ! -d "/home/pi/.pip/" ];then
  mkdir /home/pi/.pip/
else
  echo "文件夹已经存在"
fi
echo -e "[global]
timeout =6000
index-url =http://pypi.douban.com/simple/
[install]
use-mirrors =true 
mirrors =http://pypi.douban.com/simple/ 
trusted-host =pypi.douban.com" > /home/pi/.pip/pip.conf
# export
export PI_LOCATION='潍坊'
# pip install

# migrate