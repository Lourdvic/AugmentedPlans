from PIL import Image

pxl_coords = []
max_x = max_y = 0

with open('pxl_coords.txt') as handle:
    for line in handle.readlines():
        x, y, hex_color = line.strip().split()
        x = int(x[1:-1])
        y = int(y[:-1])

        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)

        pxl_coords.append([x, y, r, g, b])

        max_x = max([x, max_x])
        max_y = max([y, max_y])

w = max_x + 1
h = max_y + 1
size = w, h

plan = Image.new('RGB', size)

data = plan.load()

for pxl_coord in pxl_coords:
    x, y, r, g, b = pxl_coord

    data[x, y] = (r, g, b)

plan.show()
plan.save('plan_recreated.jpg')