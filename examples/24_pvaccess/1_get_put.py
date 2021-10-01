from p4p.client.thread import Context
from time import sleep

pva = Context('pva')

print("Setpoint:", pva.get('training:setpoint'))
print("Tank temperature:")
for i in range(10):
    print(pva.get('training:tank'))
    sleep(1)

pva.put('training:setpoint', 40)
print("Setpoint:", pva.get('training:setpoint'))

print("Tank temperature:")
for i in range(10):
    print(pva.get('training:tank'))
    sleep(1)

pva.put('training:setpoint', 30)

