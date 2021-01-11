import sys

line = sys.stdin.readline()
up = 0
down = 0
for i in line:
    if i == '(':
        up += 1
    elif i == ')':
        down += 1
print(up - down)

floor = 0
for i in range(len(line)):
    if line[i] == '(':
        floor += 1
    elif line[i] == ')':
        floor -= 1
    if floor == -1:
        print(i + 1)
        break
