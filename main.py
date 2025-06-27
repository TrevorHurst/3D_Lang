class Plane:
    def __init__(s, vals):
        s.rows = ''.join(vals).split('\n')
    def at(s, x,y):
        try:
            return s.rows[y][x]
        except:
            return None
    def put(s,x,y,val):
        while len(s.rows) < y:
            s.rows.append([''])
        while len(s.rows[y]) < x:
            s.rows[y]+=' '
        s.rows[y] = s.rows[y][:x]+val+s.rows[y][x+1:]
            
def geta(vals):
    global planes
    x,y,z = vals
    try:
        return planes[z].at(x,y)
    except:
        return None
def put(info):
    global planes
    val,x,y,z = info
    while len(planes) < z:
        planes.append(Plane(['']))
    planes[z].put(x,y,chr(val))
def newcord():
    global cord, direction
    if direction == 0:
        cord[0]+=1
    if direction == 1:
        cord[0]-=1
    if direction == 2:
        cord[1]-=1
    if direction == 3:
        cord[1]+=1
    if direction == 4:
        cord[2]+=1
    if direction == 5:
        cord[2]-=1
try:
    i=0
    planes = []
    while True:
        planes.append(Plane(
            open(f'plane{i}.3D','r+').readlines()))
        i+=1
except:
    pass
coder = {
    '<': 'direction = 1',
    '>': 'direction = 0',
    '^': 'direction = 2',
    'v': 'direction = 3',
    '}': 'direction = 4',
    '{': 'direction = 5',
    '#': 'stack.pop(0)',
    '&': 'running = False',
    '$': 'newcord()',
    '@': 'newcord();newcord()',
    '~': 'stack[0],stack[1]=[stack[1],stack[0]]',
    '|': 'direction = 2 if stack[0]>stack[1] else 3;stack=stack[2:]',
    '?': 'direction = 1 if stack[0]>stack[1] else 0;stack=stack[2:]',
    '!': 'direction = 4 if stack[0]>stack[1] else 5;stack=stack[2:]',
    '#': 'stack.pop(0)',
    '=': 'stack.insert(0,stack[0])',
    '+': 'stack[0]+=stack[1];stack.pop(1)',
    '-': 'stack[1]-=stack[0];stack.pop(0)',
    '*': 'stack[0]*=stack[1];stack.pop(1)',
    '/': 'stack[1]/=stack[0];stack.pop(0)',
    '.': "print(stack[0],end='');stack.pop(0)",
    ',': "print(chr(stack[0]),end='');stack.pop(0)",
    "'": 'stringmode = True',
    'g': 'stack.insert(3,ord(geta(stack[:3])));stack=stack[3:]',
    'p': 'put(stack[:4]);stack=stack[4:]',
    ')': "stack.insert(0,int(input('number: ')))",
    '(': "stack.insert(0,ord(input('character: ')))",
    '%': 'running=False'
}

# directions are 0 - right, 1 - left, 2 - up, 3 - down, 4 nxt, 5, prev
direction = 0
cord = [0,0,0]
stack = [0 for i in range(20)]
running = True
stringmode = False
while running:
    if not stringmode:
        try:
            exec(coder[geta(cord)])
        except:
            try:
                stack.insert(0,int(geta(cord)))
            except:
                pass

        while len(stack) < 5:
            stack.append(0)
    else:
        while geta(cord) != "'":
            stack.insert(0,ord(geta(cord)))
            newcord()
        stringmode=False
    newcord()
print()