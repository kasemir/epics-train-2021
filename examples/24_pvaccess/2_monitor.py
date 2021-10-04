from p4p.client.thread import Context
from time import sleep

pva = Context('pva')

def show_setpoint(V):
    print("Setpoint:", V)

def show_temperature(V):
    print("Tank temperature:", V)

# pva.monitor('name_of_pv') returns a subscripion.
# We need to hold on to it, because otherwise the garbage collector
# will close it an any time.
# There are two ways to handle subscriptions
# 1) Hold on to the subscription in a variable and later 'close()' it.
subcription1 = pva.monitor('training:setpoint', show_setpoint)

# 2) Use in a 'with pv.monitor(...), pva.monitor(...):'
#    block which will internally keep the subscription
#    and close when leaving the scope
with pva.monitor('training:tank', show_temperature):
    sleep(10)
    print("Changing setpoint...")
    pva.put('training:setpoint', 40)

    sleep(10)
    print("Changing setpoint...")
    pva.put('training:setpoint', 30)

subcription1.close()
