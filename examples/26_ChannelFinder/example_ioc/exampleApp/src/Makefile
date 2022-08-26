TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = example
DBD += example.dbd
example_DBD += base.dbd
example_DBD += reccaster.dbd
example_LIBS += reccaster

example_SRCS += example_registerRecordDeviceDriver.cpp

example_SRCS_DEFAULT += exampleMain.cpp
example_SRCS_vxWorks += -nil-

example_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

