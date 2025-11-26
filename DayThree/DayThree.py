north = "^"
south = "v"
east = ">"
west = "<"

x, y = 0, 0
v, z = 0, 0
i = 0

s = {(x, y)}

with open('input.txt', 'r') as input:
    for ch in input.read().strip():
        if i == 0:
            if ch == north:
                y += 1
            elif ch == south:
                y -= 1
            elif ch == east:
                x += 1
            elif ch == west:
                x -= 1
            i += 1
            s.add((x,y))
        elif i == 1:
            if ch == north:
                v += 1
            elif ch == south:
                v -= 1
            elif ch == east:
                z += 1
            elif ch == west:
                z -= 1
            i -= 1
            s.add((z,v))
    print(s)
    print(len(s))




#Read the input in from the file
#using a set to mark which coordinates (houses) have been visited
    #a set doesn't allow duplicate values which is good here because we only need to the count the house visit once
#with each character in the input, update the coordinate value, then add that to the set
#print length of set to get number of houses visited


#Part Two
#Add a bit that flips with each ch
#Create a separate if statement, one for each santa
#two sets, one for each santa
#at the end compare the sets and get rid of the same coordinates
#print length of the set that is the combination of the other two