TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Use typed rset structure (see 3.16.1 release notes)
USR_CPPFLAGS += -DUSE_TYPED_RSET

# Build the IOC application
PROD_IOC = seq

# seq.dbd will be created and installed
DBD += seq.dbd

# seq.dbd will include these files:
seq_DBD += base.dbd

# seq_registerRecordDeviceDriver.cpp derives from seq.dbd
seq_SRCS += seq_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
seq_SRCS_DEFAULT += seqMain.cpp
seq_SRCS_vxWorks += -nil-

# Build sncExample into seqSupport
SNCFLAGS += +r
seq_DBD += sncExample.dbd

# A .stt sequence program is *not* pre-processed:
# seq_SRCS += sncExample.stt
seq_SRCS += sncProgram.st

seq_DBD += tank.dbd
seq_SRCS += tank.st

seq_LIBS += seq pv

# Link QSRV (pvAccess Server) if available
seq_LIBS += qsrv
seq_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
seq_DBD += PVAServerRegister.dbd
seq_DBD += qsrv.dbd

# Finally link IOC to the EPICS Base libraries
seq_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

