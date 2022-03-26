#!/bin/bash
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y redis 
mkdir /home/pi/.pip/
echo -e "[global]
timeout =6000
index-url =http://pypi.douban.com/simple/
[install]
use-mirrors =true 
mirrors =http://pypi.douban.com/simple/ 
trusted-host =pypi.douban.com" > /home/pi/.pip/pip.conf