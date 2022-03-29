#!/bin/bash -e
# update repo
#sudo apt update -y
#sudo apt upgrade -y
# install app
#sudo apt install -y redis
# 创建pip配置文件
if [ ! -d "/home/pi/.pip/" ];then
  mkdir /home/pi/.pip/
fi
echo -e "[global]
timeout =6000
index-url =http://pypi.douban.com/simple/
[install]
use-mirrors =true 
mirrors =http://pypi.douban.com/simple/ 
trusted-host =pypi.douban.com" > /home/pi/.pip/pip.conf
# export
export PI_LOCATION='莒南'
# pip install

# migrate
# 开机启动浏览器
if [ ! -d "/home/pi/.config/autostart" ];then
  mkdir -p /home/pi/.config/autostart
fi
echo -e '[Desktop Entry]
Type=Application
Exec=chromium-browser  --disable-popup-blocking --no-first-run --disable-desktop-notifications  --kiosk "http://127.0.0.1:5555"'> /home/pi/.config/autostart/my.desktop # todo port

# run
echo -e '[Desktop Entry]
Name=magic_mirror
Comment=magic mirror launch
Exec=python3 /home/pi/magic_mirror/run.py
Terminal=true
MultipleArgs=False
Type=Application
Categories=Application;Development;
StartupNotify=true
'>/home/pi/.config/autostart/magic_mirror.desktop
