#!../../bin/linux-x86_64/streamDemo

< envPaths

## Register all support components
dbLoadDatabase("../../dbd/streamDemo.dbd",0,0)
streamDemo_registerRecordDeviceDriver(pdbbase)

epicsEnvSet ("STREAM_PROTOCOL_PATH", "/ics/examples/08_streamDemoApp/Db")

drvAsynIPPortConfigure ("SI", "127.0.0.1:24742")

# Log some asyn info and in/out texts
# ASYN_TRACE_ERROR     0x0001
# ASYN_TRACEIO_DEVICE  0x0002
# ASYN_TRACEIO_FILTER  0x0004
# ASYN_TRACEIO_DRIVER  0x0008
# ASYN_TRACE_FLOW      0x0010
# ASYN_TRACE_WARNING   0x0020
asynSetTraceMask("SI", 0, 4)
asynSetTraceIOMask("SI", 0, 6)

## Load record instances
dbLoadRecords("../../db/si_stream.db")

iocInit()

