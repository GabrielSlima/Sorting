import random

def order(list):
    listLen = len(list)
    print("List has {} items".format(listLen))
    for i in range(listLen -1 ,-1, -1):
        for j in range(0, i):
            print(str(list[i]) + " < " + str(list[j]) + ": " + str(list[i] < list[j]))
            if list[i] < list[j]:
                changeToJPosition = list[i]
                changeToIPosition = list[j]
                list[i] = changeToIPosition
                list[j] = changeToJPosition
    return list

firstList = [4,8,123,2]
print("Fisrt list: {} ".format(firstList))
print(order(firstList))

secondList = []

for i in range(0, 20):
    secondList.append(random.randint(0, 2000))

print("--------- SECOND LIST: {}".format(secondList))
print(order(secondList))
