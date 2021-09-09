#!../../bin/linux-x86_64/autosave

< envPaths

## Register all support components
dbLoadDatabase("../../dbd/autosave.dbd",0,0)
autosave_registerRecordDeviceDriver(pdbbase) 

## Load record instances

### AUTOSAVE: Load autosave status DB (optional) #####
#cd $(AUTOSAVE)
#dbLoadRecords("db/save_restoreStatus.db","P=demo:")
######################################################

# "Normal" records of this IOC
cd $(TOP)
dbLoadRecords("db/autosave.db","S=demo")

### AUTOSAVE: Configure ###############################
# File locations, using some macros
#epicsEnvSet IOCNAME autosave_demo
#epicsEnvSet SAVE_DIR /ics/examples/iocBoot/ioc_autosave
#save_restoreSet_status_prefix("demo:")
#set_requestfile_path("$(SAVE_DIR)")
#set_savefile_path("$(SAVE_DIR)")

# Schedule a maximum of 3 sequenced backups of the .sav file
# every 10 minutes - .sav0, .sav1, .sav2
#save_restoreSet_NumSeqFiles(3)
#save_restoreSet_SeqPeriodInSeconds(600)

# Arrange for restoring saved values into records
#set_pass1_restoreFile("$(IOCNAME).sav")
######################################################


# Start IOC processes
iocInit()


### AUTOSAVE: Create request file and start periodic 'save’ ##
#makeAutosaveFileFromDbInfo("$(SAVE_DIR)/$(IOCNAME).req", "autosaveFields")
#create_monitor_set("$(IOCNAME).req", 5)
######################################################
