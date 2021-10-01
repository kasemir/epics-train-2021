# Read PV from 'makeBaseApp.pl -t example'
# to check if circle.x and .y are on circle

print("For faster updates,")
print("   caput training:circle:period 0.2")
 
from p4p.client.thread import Context
from time import sleep
from math import sqrt

pva = Context('pva')

def check(value):
    x = value['x']['value']
    y = value['y']['value']
    print("%+.4f %+.4f -> %.8f" % (x, y, sqrt(x*x + y*y)))

pva.monitor('training:circle', check)
sleep(1000)



