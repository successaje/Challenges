def test(List, target):
    for i in range(0, len(List)-2):
        for j in range(i+1, len(List)-1):
            for k in range(j+1, len(List)):
                if List[i] + List[j] + List[k] == target:
                    print("The 3 perfect square numbers to give {0} are {1}, {2} and {3} ".format(target, List[i], List[j], List[k]))
                    return True

    return False

List = [1, 4, 68, 5, 3, 23]
target = 14
test(List, target)