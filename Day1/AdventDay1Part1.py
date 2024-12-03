
'''
2 lists measure Pair up the smallest number in the left list with the smallest number in the right list, 
then the second-smallest left number with the second-smallest right number, and so on.

Pseudocode:

- Sort lists, compare each index, Calculate the difference between them, Add together to get total distance 
'''
def loadData(list1,list2):
    with open(r"./Day1/data/input.txt","r") as file:
        for line in file:
            splitLine = line.split()
            list1.append(splitLine[0])
            list2.append(splitLine[1])
    return list1,list2

def GetDistance(list1,list2,distances):
    list1.sort()
    list2.sort()
    for values in zip(list1,list2):
        values = tuple(map(int, values))
        if values[0] >= values[1]:
            distances.append((values[0] - values[1]))
        elif values[1] >= values[0]:
            distances.append((values[1] - values[0]))
    return distances

def main():
    distances = []
    list1 = []
    list2 = []
    # list1 = [3,4,2,1,3,3]
    # list2 = [4,3,5,3,9,3]

    list1, list2 = loadData(list1, list2)
    distances = GetDistance(list1,list2,distances)
    totalDistance = sum(distances)
    print(totalDistance)


if __name__ == "__main__":
    main()