import re

ss = open("input.txt").readlines()

gg = {'red':12,'green':13,'blue':14}

game = 1
vg = {}
for s in ss:
    valid = True
    for draw in s.split(";"):
        cubes = re.findall(r'(\d+) (red|green|blue)', draw)
        
        for col in gg.keys():
            played = sum(int(i) for i, j in [(n,c) for n,c in cubes if c == col])
            if played > gg[col]:
                valid = False
    if valid:
        vg[game] = s
    
    game += 1
print(sum(vg.keys()))

p2 = 0
for s in ss:
    cubes = re.findall(r'(\d+) (red|green|blue)', s)
    l = [(int(value), color) for value, color in cubes]
    colors = {color: max(value for value, clr in l if clr == color) for _, color in l}
    p2 += colors['red']*colors['green']*colors['blue']
print(p2)