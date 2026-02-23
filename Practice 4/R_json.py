import json

with open('Practice 4/sample-data.json') as file:  
    data = json.load(file)  

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':7} {'MTU':5}")
print("-" * 80)
for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes']['descr']
    speed = interface['l1PhysIf']['attributes']['speed']
    mtu = interface['l1PhysIf']['attributes']['mtu']
    print(f"{dn:50} {description:20} {speed:7} {mtu:5}")