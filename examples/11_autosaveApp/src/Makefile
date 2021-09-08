TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = autosave
# autosave.dbd will be created and installed
DBD += autosave.dbd

# autosave.dbd will be made up from these files:
autosave_DBD += base.dbd

### Include AUTOSAVE support ###
autosave_DBD += asSupport.dbd
autosave_LIBS += autosave
################################

# autosave_registerRecordDeviceDriver.cpp derives from autosave.dbd
autosave_SRCS += autosave_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
autosave_SRCS_DEFAULT += autosaveMain.cpp
autosave_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#autosave_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
autosave_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

