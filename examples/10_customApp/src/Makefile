TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Use typed rset structure (see 3.16.1 release notes)
USR_CPPFLAGS += -DUSE_TYPED_RSET

# xxxRecord.h will be created from xxxRecord.dbd
DBDINC += xxxRecord

# Install xxxSupport.dbd into <top>/dbd
DBD += xxxSupport.dbd

# Build an IOC support library
LIBRARY_IOC += customSupport

# Compile and add code to the support library
customSupport_SRCS += xxxRecord.c
customSupport_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application, that
# causes problems on Windows DLL builds
customSupport_SRCS += dbSubExample.c
customSupport_SRCS += devcustomVersion.c
customSupport_SRCS += customHello.c
customSupport_SRCS += initTrace.c

customSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Auto-generate a header file containing a version string.
# Version comes from the VCS if available, else date+time.
GENVERSION = customVersion.h
# Macro name
GENVERSIONMACRO = customVERSION

# Build the IOC application
PROD_IOC = custom

# custom.dbd will be created and installed
DBD += custom.dbd

# custom.dbd will include these files:
custom_DBD += base.dbd
custom_DBD += xxxSupport.dbd
custom_DBD += dbSubExample.dbd
custom_DBD += devcustomVersion.dbd
custom_DBD += customHello.dbd
custom_DBD += initTrace.dbd


# custom_registerRecordDeviceDriver.cpp derives from custom.dbd
custom_SRCS += custom_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
custom_SRCS_DEFAULT += customMain.cpp
custom_SRCS_vxWorks += -nil-

# Link in the code from our support library
custom_LIBS += customSupport

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into customSupport
    sncExample_SNCFLAGS += +r
    custom_DBD += sncExample.dbd
    # A .stt sequence program is *not* pre-processed:
    customSupport_SRCS += sncExample.stt
    customSupport_LIBS += seq pv
    custom_LIBS += seq pv

    # Build sncProgram as a standalone program
    PROD_HOST += sncProgram
    sncProgram_SNCFLAGS += +m
    # A .st sequence program *is* pre-processed:
    sncProgram_SRCS += sncProgram.st
    sncProgram_LIBS += seq pv
    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Link QSRV (pvAccess Server) if available
ifdef EPICS_QSRV_MAJOR_VERSION
    custom_LIBS += qsrv
    custom_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
    custom_DBD += PVAServerRegister.dbd
    custom_DBD += qsrv.dbd
endif

# AUTOSAVE
custom_DBD += asSupport.dbd
custom_LIBS += autosave

# Finally link IOC to the EPICS Base libraries
custom_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

# Explicit dependency needed for generated header file
devcustomVersion$(DEP): $(COMMON_DIR)/$(GENVERSION)
