TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = simple

# custom.dbd will be created and installed
DBD += simple.dbd

# simple.dbd will include these files:
simple_DBD += base.dbd

# simple_registerRecordDeviceDriver.cpp derives from simple.dbd
simple_SRCS += simple_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
simple_SRCS += simpleMain.cpp

# Link QSRV (pvAccess Server) if available
simple_LIBS += qsrv
simple_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
simple_DBD += PVAServerRegister.dbd
simple_DBD += qsrv.dbd

# Finally link IOC to the EPICS Base libraries
simple_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

