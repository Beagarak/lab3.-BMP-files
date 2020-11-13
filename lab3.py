from math import cos, sin, pi


x_offset = -3
y_offset = -3
t = 0
width = 600
height = 600
all_values = []
pixel = []
STEP = 0.01
while t <= 2 * pi:
    x = round(2 * cos(t) + cos(2 * t), 2)
    y = round(2 * sin(t) - sin(2 * t), 2)
    pixel.append(x)
    pixel.append(y)
    all_values.append(tuple(pixel))
    pixel.clear()
    t += STEP

with open('test.bmp', 'w+b') as f:
    f.write(b'BM')
    f.write((154).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(2, byteorder='little'))
    f.write((0).to_bytes(2, byteorder='little'))

    f.write((122).to_bytes(4, byteorder='little'))
    f.write((108).to_bytes(4, byteorder='little'))
    f.write((600).to_bytes(4, byteorder='little'))
    f.write((600).to_bytes(4, byteorder='little'))
    f.write((1).to_bytes(2, byteorder='little'))
    f.write((32).to_bytes(2, byteorder='little'))
    f.write((3).to_bytes(4, byteorder='little'))
    f.write((32).to_bytes(4, byteorder='little'))
    f.write((2835).to_bytes(4, byteorder='little'))
    f.write((2835).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))

    f.write(b'\x00\x00\xFF\x00')
    f.write(b'\x00\xFF\x00\x00')
    f.write(b'\xFF\x00\x00\x00')
    f.write(b'\x00\x00\x00\xFF')

    f.write(b' niW')
    f.write((0).to_bytes(36, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))
    f.write((0).to_bytes(4, byteorder='little'))

    for y_counter in range(600):
        x_offset = -3
        for x_counter in range(600):
            if (x_offset, y_offset) in all_values:
                f.write(b'\x00\x00\x00\xFF')
            else:
                f.write(b'\xFF\xFF\xFF\xFF')
            x_offset = round(x_offset + STEP, 2)
        y_offset = round(y_offset + STEP, 2)
    f.close()