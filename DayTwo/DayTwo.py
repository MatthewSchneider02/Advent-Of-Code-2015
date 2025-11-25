runningTotal = 0
extraPaper = 0
arr = []
totalRibbon = 0
ribbon = 0

with open('input.txt', 'r') as input:
    for line in input:
        arr.append(line.rstrip())

for x in arr:
    dimensions = x.split('x')
    l = int(dimensions[0])
    w = int(dimensions[1])
    h = int(dimensions[2])
    #This line would be better: l, w, h = map(int, x.split('x')) and would get rid of the three lines above

    dimensionsOne = l * w
    dimensionsTwo = w * h
    dimensionsThree = l * h
    extraPaper = min(dimensionsOne, dimensionsTwo, dimensionsThree)
    runningTotal += 2 * (dimensionsOne + dimensionsTwo + dimensionsThree) + extraPaper

    largestDimension = max(l, w, h)
    ribbon = (l * w * h) + 2 * (l + w + h - largestDimension)
    totalRibbon += ribbon

print(runningTotal)
print(totalRibbon)

#Because each input is num x num x num we need to break it up line by line
#Go line by line, reading each in, split up by the x
#for each newline
#split into array and find the smallest num, add to running total
#multiply each by 2 then multiply arr[0] and arr[1], arr[1] and arr[2], and arr[0] arr[2], then add together
#add to running total and continue to next line


#Part 2
#Need the perimeter of the smallest side
    #take the two smallest dimensions, add them, and multiply by 2
    #would it be easier to find the largest side, add all the sides, then subtract the longest?
#l*w*h for the bow
