#!../../bin/linux-x86_64/simple

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/simple.dbd"
simple_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords "db/simple.db", "user=training"

cd "${TOP}/iocBoot/${IOC}"
iocInit

