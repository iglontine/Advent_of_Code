import sys

commands = sys.stdin.readline().strip().split(", ")

x = 0
y = 0
f = 'N'
visited = [(x, y)]

# for i in range(len(commands)):
#     command = commands[i]
for command in commands:
    if command[0] == 'R':
        if f == 'N':
            f = 'E'
        elif f == 'E':
            f = 'S'
        elif f == 'S':
            f = 'W'
        elif f == 'W':
            f = 'N'
    elif command[0] == 'L':
        if f == 'N':
            f = 'W'
        elif f == 'W':
            f = 'S'
        elif f == 'S':
            f = 'E'
        elif f == 'E':
            f = 'N'
    steps = int(command[1:])
    for i in range(steps):
        if f == 'N':
            y += 1
        elif f == 'E':
            x += 1
        elif f == 'S':
            y -= 1
        elif f == 'W':
            x -= 1
        if (x, y) in visited:
            print(abs(x) + abs(y))
        else:
            visited.append((x, y))
print(abs(x) + abs(y))
