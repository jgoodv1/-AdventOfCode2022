SAND_ENTRY = (500,0)
CAVE = set()
MAX_Y = 0

def maxy(y):
    global MAX_Y
    if y > MAX_Y:
        MAX_Y = y


with open("input14.txt") as fin:
    lines = fin.read().strip().split("\n")

def draw_cave():
    global lines, CAVE
    CAVE = set()
    for line in lines:
        rocks = []
    
        for str_coord in line.split(" -> "):
            x, y = str_coord.split(",")
            rocks.append((int(x), int(y)))
          
        for i in range(1, len(rocks)):
            x1, y1 = rocks[i]
            x0, y0 = rocks[i - 1]
    
            if x1 != x0:
                maxy(y1)
                for x in range(min(x0, x1), max(x0, x1) + 1):
                    CAVE.add((x, y1))
            else:
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    maxy(y)
                    CAVE.add((x1, y))

def pour_sand(part):
    global CAVE, SAND_ENTRY, MAX_Y
    draw_cave()
    if part == 2:
        add_floor()
        
    count = 0
    x, y = SAND_ENTRY
    while y <= MAX_Y:

        if (x, y + 1) not in CAVE:
            y += 1
            continue

        if (x - 1, y + 1) not in CAVE:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in CAVE:
            x += 1
            y += 1
            continue

        count += 1
        if (x,y) == SAND_ENTRY:
            print('break')
            break
        
        CAVE.add((x,y))
        x, y = SAND_ENTRY
        

    return count

def add_floor():
    global MAX_Y
    MAX_Y += 2
    
    for x in range(MAX_Y * -5, MAX_Y * 5):
        CAVE_FILLED.add((x, MAX_Y))
    

print(pour_sand(1))
print(pour_sand(2))