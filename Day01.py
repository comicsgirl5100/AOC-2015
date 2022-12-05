import utils

day = "01"
test1Solution = -1
test2Solution = 5

def finalFloor(directions):
    floor = 0
    for step in directions:
        if step == "(":
            floor += 1
        else:
            floor += -1
    return floor


def part1(input):
    for directions in input:
        return finalFloor(directions)


def inBasement(directions):
    floor = 0
    stepNumber = 0
    for step in directions:
        if step == "(":
            floor += 1
        else:
            floor -= 1
        stepNumber += 1
        if floor < 0:
            return stepNumber

def part2(input):
    for directions in input:
        return inBasement(directions)


if __name__ == "__main__":
    try:
        testData = utils.readTestData(day)
        test1Answer = part1(testData)
        if test1Answer == test1Solution:
            print("Test 1 pass")
        else:
            print(f"got {test1Answer}, but expected {test1Solution}")

        test2Answer = part2(testData)
        if test2Answer == test2Solution:
            print("Test 2 pass")
        else:
            print(f"got {test2Answer}, but expected {test2Solution}")


    except FileNotFoundError:
        print("No test data")

    try:
        data = utils.readData(day)
        part1Solution = part1(data)
        print(f"part1: {part1Solution}")

        part2Solution = part2(data)
        print(f"part2: {part2Solution}")

    except FileNotFoundError:
        print("No problem input")
