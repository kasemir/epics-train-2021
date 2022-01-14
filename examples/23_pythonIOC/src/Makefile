TOP=../..

include $(TOP)/configure/CONFIG
include $(PYDEVICE)/configure/CONFIG.PyDevice
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = pyioc

# custom.dbd will be created and installed
DBD += pyioc.dbd

# pyioc.dbd will include these files:
pyioc_DBD += base.dbd
pyioc_DBD += pydev.dbd
pyioc_DBD += pycalcRecord.dbd

# pyioc_registerRecordDeviceDriver.cpp derives from pyioc.dbd
pyioc_SRCS += pyioc_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
pyioc_SRCS += pyiocMain.cpp

# Finally link IOC to the EPICS Base libraries
pyioc_LIBS += $(EPICS_BASE_IOC_LIBS)
pyioc_LIBS += pydev

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

