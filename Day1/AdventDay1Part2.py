'''
Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
'''


def loadData(list1,list2):
    with open(r"./Day1/data/input.txt","r") as file:
        for line in file:
            splitLine = line.split()
            list1.append(int(splitLine[0]))
            list2.append(int(splitLine[1]))
    return list1,list2

def GetFrequency(list2,numFreqency):
    for num in list2:
        numFreqency[num] = numFreqency.get(num,0) + 1
    return numFreqency

def CalcualteSimilartyScore(list1,numFreqency):
    similartyscores = []
    for num in list1:
        if num in numFreqency:
            # print(f"{num} * {numFreqency[num]}")
            similartyscores.append(num * numFreqency[num])
        else:
            # If num is not in the frequency dictionary we would multiply by 0, since we don't need to we append 0
            similartyscores.append(0)

    return similartyscores


def main():
    list1 = []
    list2 = []
    # list1 = [3,4,2,1,3,3]
    # list2 = [4,3,5,3,9,3]
    numFreqency = {}
    totalSimilarity = 0

    list1, list2 = loadData(list1, list2)
    numFreqency = GetFrequency(list2,numFreqency)
    
    totalSimilarity = CalcualteSimilartyScore(list1,numFreqency)
    print(sum(totalSimilarity))


if __name__ == "__main__":
    main()