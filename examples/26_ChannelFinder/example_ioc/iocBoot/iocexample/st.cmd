#!../../bin/linux-x86_64/example

#- You may have to change example to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/example.dbd"
example_registerRecordDeviceDriver pdbbase

epicsEnvSet("IOCNAME", "TrainingIOC")
epicsEnvSet("ENGINEER", "Bob")
epicsEnvSet("LOCATION", "Rack 123")

## Load record instances
dbLoadRecords("db/demo.db")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=training"
