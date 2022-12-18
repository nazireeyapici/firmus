def areSame(float1, float2):
    return abs(float1 - float2) < 0.001
    
def lengths(ls):
    return (abs(ls[0] - ls[2]), abs(ls[1] - ls[3]))

def inRange(num, limits):
    limits.sort()
    return areSame(num, limits[0]) or areSame(num, limits[1]) or limits[0] < num < limits[1]

def collapsingRangeLength(range1, range2):
    range1.sort()
    range2.sort()
    ranges = []
    
    for i in range1:
        if inRange(i, range2):
            ranges.append(i)
    for i in range2:
        if inRange(i, range1):
            ranges.append(i)
    
    return abs(ranges[0] - ranges[1])

def massCenter(ls):
    return ((ls[0] + ls[2]) / 2, (ls[1] + ls[3]) / 2)

def overlappingArea(list1, list2):
    width = collapsingRangeLength(list1[::2], list2[::2])
    height = collapsingRangeLength(list1[1::2], list2[1::2])
    
    return width * height

def area(list1, list2):
    area1, area2 = 1, 1
    for i in lengths(list1):
        area1 *= i
    for i in lengths(list2):
        area2 *= i
    
    return area1 + area2 - overlappingArea(list1, list2)

def smallestBlock(upper, floor):
    floor.sort()
    center = (upper[0] + upper[2]) / 2
    if abs(center - floor[0]) < abs(center - floor[1]):
        center = 0
    else:
        center = 1
    
    vertices = upper[::2]
    vertices.sort()
    
    vertice = 2 * floor[center] - vertices[center]
    
    return [vertices[1 - center], upper[1], vertice, upper[3]]
    
def is_firmus(list1, list2):
    assert (type(list1) is type([])) and (type(list2) is type([])), "Arguments' types should be list"
    assert len(list1) == 4 and len(list2) == 4, "Lists should have 4 items"
    
    lower, upper = [list1, list2] if list1[1] + list1[3] < list2[1] + list2[3] else [list2, list1]
    
    onFloor = False
    coincidingEdges = False
    stable = False
    
    if lower[1] == 0 or lower[2] == 0:
        onFloor = True
    if areSame(min(upper[1::2]), max(lower[1::2])):
        coincidingEdges = True
    if coincidingEdges:
        stable = inRange(massCenter(upper)[0], lower[::2])
    
    if onFloor and coincidingEdges and stable:
        return ["FIRMUS", area(list1, list2)]
    if onFloor and coincidingEdges and not stable:
        block = smallestBlock(upper, lower[::2])
        return ["ADDENDUM", block]
    
    return ["DAMNARE", area(list1, list2)]

print(is_firmus([-0.5, 10, -6, 13], [-7, 0, 3, 10]))
print(is_firmus([-8, 11, 2, 5], [1, 0, -2, 5]))
print(is_firmus([0, 0, 2.4, 5.2], [-8.7, 10, 0, 0]))