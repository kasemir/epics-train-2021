TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

# Use typed structures (see 3.16.1 release notes)
USR_CPPFLAGS += -DUSE_TYPED_RSET -DUSE_TYPED_DSET

PROD_IOC = deviceSupport
# deviceSupport.dbd will be created and installed
DBD += deviceSupport.dbd

# deviceSupport.dbd will be made up from these files:
deviceSupport_DBD += base.dbd
deviceSupport_DBD += my_device.dbd

# deviceSupport_registerRecordDeviceDriver.cpp derives from deviceSupport.dbd
deviceSupport_SRCS += deviceSupport_registerRecordDeviceDriver.cpp
deviceSupport_SRCS += devAiRnd.c
deviceSupport_SRCS += drvRandom.c

# Build the main IOC entry point on workstation OSs.
deviceSupport_SRCS_DEFAULT += deviceSupportMain.cpp
deviceSupport_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#deviceSupport_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
deviceSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

