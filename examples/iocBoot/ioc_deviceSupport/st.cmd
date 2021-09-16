#!../../bin/linux-x86_64/deviceSupport

## Register all support components
dbLoadDatabase("../../dbd/deviceSupport.dbd",0,0)
deviceSupport_registerRecordDeviceDriver(pdbbase) 

## Load record instances
dbLoadRecords("../../db/my_device.db","user=demo")

iocInit()

