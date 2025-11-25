floor = 0
basementPosition = 0

with open('input.txt', 'r') as input:
    arr = list(input.read())

for i, ch in enumerate(arr):
    if ch == ("("):
        floor+=1
    else:
        floor-=1

    if floor < 0 and basementPosition == 0:
        basementPosition = i + 1

print(floor)
print(basementPosition)