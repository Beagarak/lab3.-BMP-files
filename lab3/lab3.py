import math
from math import cos as cos
from math import sin as sin

x1 = -3
y1 = -3
t = 0
width = 600
height = 600
all_values = []
pixel = []

while t <= 2 * math.pi:
    x = round(2 * cos(t) + cos(2 * t), 2)
    y = round(2 * sin(t) - sin(2 * t), 2)
    pixel.append(x)
    pixel.append(y)
    all_values.append(tuple(pixel))
    pixel.clear()
    t += 0.01

with open("test.bmp", "w+b") as f:
    f.write(b'BM')
    f.write((154).to_bytes(4, byteorder="little"))
    f.write((0).to_bytes(2, byteorder="little"))
    f.write((0).to_bytes(2, byteorder="little"))

    f.write((122).to_bytes(4, byteorder="little"))
    f.write((108).to_bytes(4, byteorder="little"))
    f.write((600).to_bytes(4, byteorder="little"))
    f.write((600).to_bytes(4, byteorder="little"))
    f.write((1).to_bytes(2, byteorder="little"))
    f.write((32).to_bytes(2, byteorder="little"))
    f.write((3).to_bytes(4, byteorder="little"))
    f.write((32).to_bytes(4, byteorder="little"))
    f.write((2835).to_bytes(4, byteorder="little"))
    f.write((2835).to_bytes(4, byteorder="little"))
    f.write((0).to_bytes(4, byteorder="little"))
    f.write((0).to_bytes(4, byteorder="little"))

    f.write(b'\x00\x00\xFF\x00')
    f.write(b'\x00\xFF\x00\x00')
    f.write(b'\xFF\x00\x00\x00')
    f.write(b'\x00\x00\x00\xFF')

    f.write(b' niW')
    f.write((0).to_bytes(36, byteorder="little"))
    f.write((0).to_bytes(4, byteorder="little"))
    f.write((0).to_bytes(4, byteorder="little"))
    f.write((0).to_bytes(4, byteorder="little"))

    for i in range(600):
        x1 = -3
        for j in range(600):
            if (x1, y1) in all_values:
                f.write(b'\x00\x00\x00\xFF')
            else:
                f.write(b'\xFF\xFF\xFF\xFF')
            x1 = round(x1 + 0.01, 2)
        y1 = round(y1 + 0.01, 2)
    f.close()