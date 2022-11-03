import bluetooth

target_name = ("my phone")
target_address = None

nearby_devices = bluetooth.discover_devices()
for bddadr in nearby_devices:
  if target_name == bluetooth.lookup_name ( bddadr ):
    target_address = bdaddr
  break
if target_address is not None:
  print ("nearby devices found", target_address)
else:
    print ("no devices found")
