#!../../bin/linux-x86_64/pyioc

< envPaths

# PYTHONPATH points to folders where Python modules are.
epicsEnvSet("PYTHONPATH","$(TOP)/python")

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/pyioc.dbd"
pyioc_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords "db/pyioc.db", "user=training:pydevice"
dbLoadRecords "db/weather.db", "user=training"

cd "${TOP}/iocBoot/${IOC}"
pydev "import demo"
pydev "from math import *"
pydev "from weather import getWeather"
iocInit

