from smbus2 import SMBus

with SMBus(1) as bus:
    # Write a byte to address 80, offset 0
    data = 45
    bus.write_byte_data(9, 0, data)
