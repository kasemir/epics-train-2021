Recipe for setting up tools
===========================

Contains all the tools: EPICS base, asyn, CS-Studio, ...

Run /ide/etc/setup.sh for each new bash:

    echo source /ics/etc/setup.sh >>~/.bashrc

Sundry
------

Misc. Debian additions:

    sudo apt install htop
    sudo apt install git
    sudo apt install make
    sudo apt install g++
    sudo apt install python3-is-python

Set background

    gsettings set org.gnome.desktop.background picture-uri file:////ics/EPICS.png
    gsettings set org.gnome.desktop.background picture-options centered
or
    gsettings set org.gnome.desktop.background picture-options scaled

Disable update prompts:
Applications, Settings, Notifications, Software Updater:
Turn all details off.

Perform manual update via Appllications, Software Update.

EPICS
-----

```
# Base
sudo apt install libreadline-dev
cd /ics/tools
wget https://epics.anl.gov/download/base/base-7.0.6.tar.gz
tar vzxf base-7.0.6.tar.gz
rm vzxf base-7.0.6.tar.gz
cd base-7.0.6
make
echo "EPICS_BASE=`pwd`" > ../RELEASE.local


# EtherIP
cd /ics/tools
git clone https://github.com/EPICSTools/ether_ip.git
cd ether_ip
make
echo "ETHER_IP=`pwd`" >> ../RELEASE.local

# Sequencer
sudo apt install re2c
cd /ics/tools
wget https://www-csr.bessy.de/control/SoftDist/sequencer/releases/seq-2.2.9.tar.gz
tar vzxf seq-2.2.9.tar.gz 
rm seq-2.2.9.tar.gz 
cd seq-2.2.9/
make
echo "SNCSEQ=`pwd`" >> ../RELEASE.local

# Autosave
cd /ics/tools
wget https://github.com/epics-modules/autosave/archive/R5-10-2.zip
unzip R5-10-2.zip
rm R5-10-2.zip 
cd autosave-R5-10-2
make
echo "AUTOSAVE=`pwd`" >> ../RELEASE.local

# Asyn
cd /ics/tools
wget https://epics.anl.gov/download/modules/asyn4-38.tar.gz
tar vzxf asyn4-38.tar.gz
rm asyn4-38.tar.gz
cd asyn4-38
cp ../ether_ip/configure/RELEASE configure
make
echo "ASYN=`pwd`" >> ../RELEASE.local

# Stream Device
cd /ics/tools
wget https://github.com/paulscherrerinstitute/StreamDevice/archive/master.zip
unzip master.zip
rm master.zip
cd StreamDevice-master
cp ../ether_ip/configure/RELEASE configure
make
echo "STREAM=`pwd`" >> ../RELEASE.local


# Busy record
cd /ics/tools
wget https://epics.anl.gov/bcda/synApps/tar/busy_R1-6-1.tar.gz
tar vzxf busy_R1-6-1.tar.gz
rm busy_R1-6-1.tar.gz
cd busy-1-6-1
cp ../ether_ip/configure/RELEASE configure
make
echo "BUSY=`pwd`" >> ../RELEASE.local


# Area Detector
sudo apt install zlib1g-dev
cd /ics/tools
wget https://github.com/areaDetector/areaDetector/archive/refs/tags/R3-11.zip
unzip R3-11.zip 
rm R3-11.zip 
mv areaDetector-R3-11 areaDetector

wget https://github.com/areaDetector/ADCore/archive/refs/tags/R3-11.zip
unzip R3-11.zip 
mv ADCore-R3-11/* areaDetector/ADCore
rm R3-11.zip 
rm -rf ADCore-R3-11

wget https://github.com/areaDetector/ADSupport/archive/refs/tags/R1-10.zip
unzip R1-10.zip
mv ADSupport-R1-10/* areaDetector/ADSupport/
rm -rf ADSupport-R1-10
rm R1-10.zip 

wget https://github.com/areaDetector/ADSimDetector/archive/R2-10.zip
unzip R2-10.zip 
mv ADSimDetector-R2-10/* areaDetector/ADSimDetector/
rm -rf ADSimDetector-R2-10/
rm R2-10.zip 

wget https://github.com/areaDetector/pvaDriver/archive/refs/tags/R1-5.zip
unzip R1-5.zip
rm R1-5.zip
mv pvaDriver-R1-5/* areaDetector/pvaDriver/
rm -rf pvaDriver-R1-5

cd areaDetector
# See https://areadetector.github.io/master/install_guide.html,
# edit many configure/* files
make


# PyEpics CA client
sudo apt install python3-pip
cd /ics/tools
wget https://github.com/pyepics/pyepics/archive/refs/tags/3.5.0.zip
unzip 3.5.0.zip
rm 3.5.0.zip
cd pyepics-3.5.0
python setup.py build
sudo python setup.py install
cd ..
sudo rm -rf pyepics-3.5.0
```

CS-Studio
---------

Install JDK from http://jdk.java.net/ into /ics/tools/jdk.

Phoebus
```
cd /ics/tools
mkdir phoebus
cd phoebus

wget https://controlssoftware.sns.ornl.gov/css_phoebus/nightly/product-sns-linux.zip
unzip product-sns-linux.zip
rm product-sns-linux.zip
rm product-*/lib/app-update-*.jar 
```

Example Displays
```
rm -rf "/ics/opi/Display Builder"
css
# Applications, Display, Examples, Install in /ics/opi
# i.e. creating /ics/opi/Display Builder
```

VDCT
```
cd /ics/tools
wget https://github.com/epics-extensions/VisualDCT/releases/download/v2.8.2/VisualDCT-2.8.2-distribution.tar.gz
tar vzxf VisualDCT-2.8.2-distribution.tar.gz
rm VisualDCT-2.8.2-distribution.tar.gz
```

Display Builder Web Runtime
```
cd /ics/tools
wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.52/bin/apache-tomcat-9.0.52.zip
unzip apache-tomcat-9.0.52.zip
rm apache-tomcat-9.0.52.zip
chmod +x apache-tomcat-9.0.52/bin/*.sh

wget https://apache.osuosl.org//ant/binaries/apache-ant-1.10.11-bin.zip
unzip apache-ant-1.10.11-bin.zip
rm apache-ant-1.10.11-bin.zip
ln -s /ics/tools/apache-ant-1.10.11/bin/ant /ics/bin

git clone https://github.com/kasemir/pvws.git
cd pvws
rm -rf .git
export CATALINA_HOME=/ics/tools/apache-tomcat-9.0.52
ant
mv pvws.war ../apache-tomcat-9.0.52/webapps
ant clean

cd /ics/tools
git clone https://github.com/kasemir/dbwr.git
cd dbwr
rm -rf .git
ant
mv dbwr.war ../apache-tomcat-9.0.52/webapps/
ant clean
```


MySQL
```
sudo apt install mariadb-server
sudo systemctl start mariadb
sudo systemctl status mariadb
# Set root password, which is initially empty, to '$root'
# Remove test database, remote root access:
sudo /usr/bin/mysql_secure_installation
sudo systemctl enable mariadb
```

MariaDB will by default not allow login as `mysql -u root -p'$root'`.
Access the RDB via `sudo mysql`,
install archive user and tables as described in
https://github.com/ControlSystemStudio/phoebus/blob/master/services/archive-engine/doc/index.rst

It will then be accessible via `mysql -u archive -p'$archive' archive`.


Archive engine
```
cd /ics/tools/phoebus
wget https://controlssoftware.sns.ornl.gov/css_phoebus/nightly/archive-engine.zip
unzip archive-engine.zip
rm archive-engine.zip
```


Alarm System
Follow https://github.com/ControlSystemStudio/phoebus/blob/master/app/alarm
```
cd /ics/tools
wget http://mirrors.gigenet.com/apache/kafka/3.0.0/kafka_2.13-3.0.0.tgz
tar -vzxf kafka_2.13-3.0.0.tgz
rm kafka_2.13-3.0.0.tgz
ln -s kafka_2.13-3.0.0 kafka

sudo mkdir /var/kafka
sudo chown training /var/kafka
# Update to use dirs under /var/kafka
vi kafka/config/zookeeper.properties
vi kafka/config/server.properties

sudo cp zookeeper.service /etc/systemd/system
sudo systemctl start zookeeper
sudo systemctl status zookeeper
netstat -an | fgrep 2181

sudo cp kafka.service /etc/systemd/system
sudo systemctl start kafka
sudo systemctl status kafka
netstat -an | fgrep 9092

sudo systemctl enable zookeeper.service
sudo systemctl enable kafka.service

sh create_alarm_topics.sh Accelerator
wget https://controlssoftware.sns.ornl.gov/css_phoebus/nightly/alarm-server.zip
unzip alarm-server.zip
rm alarm-server.zip
```
