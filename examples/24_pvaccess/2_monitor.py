from p4p.client.thread import Context
from time import sleep

pva = Context('pva')

def show_setpoint(V):
    print("Setpoint:", V)

def show_temperature(V):
    print("Tank temperature:", V)

pva.monitor('training:setpoint', show_setpoint)
pva.monitor('training:tank', show_temperature)
sleep(10)
print("Changing setpoint...")
pva.put('training:setpoint', 40)

# Need to re-start monitors after 'put'?
pva.monitor('training:setpoint', show_setpoint)
pva.monitor('training:tank', show_temperature)
sleep(10)
print("Changing setpoint...")
pva.put('training:setpoint', 30)

