TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = busy
# busy.dbd will be created and installed
DBD += busy.dbd

# busy.dbd will be made up from these files:
busy_DBD += base.dbd

# Add busy record
busy_DBD += busySupport.dbd
busy_LIBS += busy

# busy_registerRecordDeviceDriver.cpp derives from busy.dbd
busy_SRCS += busy_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
busy_SRCS_DEFAULT += busyMain.cpp
busy_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#busy_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
busy_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

