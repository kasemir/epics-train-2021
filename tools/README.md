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
```

CS-Studio
---------

Install JDK from http://jdk.java.net/ into /ics/tools/jdk.

Phoebus
```
cd /ics/tools
mkdir phoebus
cd phoebus

wget https://controlssoftware.sns.ornl.gov/css_phoebus/nightly/phoebus-linux.zip
unzip phoebus-linux.zip
rm phoebus-linux.zip
rm phoebus-*/lib/app-update-*.jar 
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



