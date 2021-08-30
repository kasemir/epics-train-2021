/* asynDemo.cpp
 * Shortest(?) example with background thread, one updating param, one config param
 */

#include <asynPortDriver.h>

/* Parameter names
 * It's customary to document the supported parameters
 * with their type and access this way in one place
 */
#define P_ValueString         "VALUE"         /* asynFloat64,  r/o */
#define P_RangeString         "RANGE"         /* asynFloat64,  r/w */


/** asynPortDriver is suggested base class for most asyn-based hardwqare access */
class asynDemo : public asynPortDriver
{
public:
    asynDemo(const char *portName);
 
private:
    // Indices used within asyn to identify a port parameter
    int P_Value;
    int P_Range;

    // Our background thread which does the actual work
    void update_code();

    static void update_code_wrapper(void *arg);
};


/** \param[in] portName The name of the asyn port driver to be created  */
asynDemo::asynDemo(const char *portName) 
   : asynPortDriver(portName, 
                    1, // how many addresses are supported on this port? 
                    asynFloat64Mask | asynDrvUserMask, // Supported 'Interfaces' (types)
                    asynFloat64Mask,  // Interrupt mask, types that support I/O Intr
                    0, // ASYN_.. flags.  This driver does not block and it is not multi-device
                    1, // Autoconnect
                    0, // Default priority
                    0) // Default stack size
{
    // Register one or more parameters for this 'port'
    createParam(P_ValueString, asynParamFloat64, &P_Value);
    createParam(P_RangeString, asynParamFloat64, &P_Range);
    
    // Set initial values
    setDoubleParam(P_Value,  0.0);
    setDoubleParam(P_Range, 10.0);
    
    // Create thread that performs value updates
    epicsThreadCreate("asynDemoTask",
                      epicsThreadPriorityMedium,
                      epicsThreadGetStackSize(epicsThreadStackMedium),
                      update_code_wrapper, this);
}

/* epicsThreadCreate(.., code, arg) needs a C function,
 * so pass this one which then calls the desired C++ method
 */
void asynDemo::update_code_wrapper(void *arg)
{
    asynDemo *self = (asynDemo *)arg;
    self->update_code();
}

void asynDemo::update_code()
{
    while (1)
    {
        // Lock when interacting with Asyn..
        double value, range;
        lock();
        getDoubleParam(P_Value, &value);
        getDoubleParam(P_Range, &range);
        unlock();
        
        // Unlock while we're busy doing something else
        value += 1;
        // Simulate that this takes a long time...
        epicsThreadSleep(5.0);
        if (value > range)
            value = 0.0;

        // Lock again for Asyn calls
        lock(); 
        updateTimeStamp();
        setDoubleParam(P_Value, value);
        callParamCallbacks();
        unlock();
    }
}


/* EPICS boilerplate for registering 'asynDemoConfigure(portName') in IOC shell */
#include <iocsh.h>
#include <epicsExport.h>
extern "C"
{

static const iocshArg initArg0 = { "portName", iocshArgString };
static const iocshArg * const initArgs[] = { &initArg0 };
static const iocshFuncDef initFuncDef = {"asynDemoConfigure", 1, initArgs };
static void initCallFunc(const iocshArgBuf *args)
{
    new asynDemo(args[0].sval);
}

void asynDemoRegister(void)
{
    iocshRegister(&initFuncDef, initCallFunc);
}

// See asynDemoInclude.dbd
epicsExportRegistrar(asynDemoRegister);

}

