#!../../bin/linux-x86_64/seq

#- You may have to change seq to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/seq.dbd"
seq_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords "db/dbExample1.db", "user=training"

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
seq sncExample, "user=training"
