#!../../bin/linux-x86_64/custom

#- You may have to change custom to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/custom.dbd"
custom_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadTemplate "db/user.substitutions"
dbLoadRecords "db/customVersion.db", "user=training"
dbLoadRecords "db/dbSubExample.db", "user=training"

dbLoadRecords "db/another.db", "user=training"

#- Set this to see messages from mySub
#var mySubDebug 1

#- Run this to trace the stages of iocInit
#traceIocInit

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
seq sncExample, "user=training"
