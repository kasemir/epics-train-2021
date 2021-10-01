from p4p.client.thread import Context
from time import sleep

pva = Context('pva')

v = pva.get('neutrons')

print("Custom Structure")
print(v)

print("\n'pixel'")
print(v['pixel'])

print("\n'pixel.value'")
print(v['pixel.value'])

print("\n'pixel', 'value'")
print(v['pixel']['value'])

