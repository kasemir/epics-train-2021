#!../../bin/linux-x86_64/busy

## Register all support components
dbLoadDatabase("../../dbd/busy.dbd",0,0)
busy_registerRecordDeviceDriver(pdbbase) 

## Load record instances
dbLoadRecords("../../db/busy_demo.db")

iocInit()
