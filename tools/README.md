Recipe for setting up tools
===========================

/ide/tools contains all the tools: EPICS base, asyn, CS-Studio, ...

/ide/etc/setup.sh, which is linked into /etc/profile.d
configures PATH etc.:

    sudo ln -s /ics/etc/setup.sh /etc/profile.d/ics.sh

Additional bash settings:

    echo "source /ics/etc/bash.rc" >> ~/.bashrc 


Sundy
-----

Misc. Debian additions:

    sudo apt install htop
    sudo apt install git
    sudo apt install build-essential

Default to bash:

    sudo rm /bin/sh
    sudo ln -s /bin/bash /bin/sh


EPICS
-----

Base:
```
sudo apt install libreadline-dev
cd /ics/tools
wget https://epics.anl.gov/download/base/base-7.0.6.tar.gz
tar vzxf base-7.0.6.tar.gz
rm vzxf base-7.0.6.tar.g
cd base-7.0.6
make
echo "EPICS_BASE=`pwd`" > ../RELEASE.local
```

EtherIP
```
cd /ics/tools
git clone https://github.com/EPICSTools/ether_ip.git
cd ether_ip
make
echo "ETHER_IP=`pwd`" >> ../RELEASE.local
```

Sequencer

```
sudo apt install re2c
cd /ics/tools
wget https://www-csr.bessy.de/control/SoftDist/sequencer/releases/seq-2.2.9.tar.gz
tar vzxf seq-2.2.9.tar.gz 
rm seq-2.2.9.tar.gz 
cd seq-2.2.9/
make
echo "SNCSEQ=`pwd`" >> ../RELEASE.local
```

Autosave
```
cd /ics/tools
wget https://github.com/epics-modules/autosave/archive/R5-10-2.zip
unzip R5-10-2.zip
rm R5-10-2.zip 
cd autosave-R5-10-2
make
echo "AUTOSAVE=`pwd`" >> ../RELEASE.local
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
# Applications, Display, Examples, Install in ~training/epics-train/examples,
# i.e. creating examples/Display Builder
```


