import time
from p4p import Type, Value
from p4p.server import Server
from p4p.server.thread import SharedPV

# Define custom data type
NEUTRONS = Type(
[
    ('charge', 'i'),
    ('pixel', 'ai'),
    ('tof', 'ai')
])

# Create a value of that type
neutrons = Value(NEUTRONS,
{
    'charge': 42,
    'pixel': [ 1, 2, 3, 4 ],
    'tof':   [ 10, 20, 30, 40 ]
})

pv = SharedPV(initial=neutrons)  

pva = Server(providers=[
{
    'demo:neutrons': pv,
}])


print("Try:")
print("pvmonitor demo:neutrons")
print("pvmonitor -r 'field(pixel)' demo:neutrons")
print("pvmonitor -r 'field(pixel,charge)' demo:neutrons")

i = 0
while True:
    i = (i+1) % 10
    update = Value(NEUTRONS,
    {
        'charge': 40+i,
        'pixel': [ i+1, i+2, i+3, i+4 ],
        'tof':   [ i+10, i+20, i+30, i+40 ]
    })
    pv.post(update)
    time.sleep(1)

pva.stop()
