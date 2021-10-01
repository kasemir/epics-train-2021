import time
from p4p.nt import NTScalar
from p4p.server import Server
from p4p.server.thread import SharedPV

# PVs that allow writing
limit = SharedPV(nt=NTScalar('d'), # scalar double
                 initial=10.0)     # setting initial value
@limit.put
def handle(pv, op):
    print("Limit changed to ", op.value())
    pv.post(op.value()) # just store and update subscribers
    op.done()

delay = SharedPV(nt=NTScalar('d'), initial=1.0)  
@delay.put
def handle(pv, op):
    print("Delay changed to ", op.value())
    pv.post(op.value()) # just store and update subscribers
    op.done()


# Read-only PVs
value = SharedPV(nt=NTScalar('d'), initial=0.0)  

pva = Server(providers=[
{
    'demo:delay': delay,
    'demo:limit': limit,
    'demo:value': value
}])


print("Try:")
print("pvmonitor demo:value")
print("pvput demo:limit 20")
print("pvput demo:delay 0.2")

i = 0
while True:
    i = i + 1
    if i > limit.current():
        i = 0
    value.post(i)
    time.sleep(delay.current())

pva.stop()
