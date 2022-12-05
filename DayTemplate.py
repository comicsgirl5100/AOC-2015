import utils

day = "00"
test1Solution = 0
test2Solution = 0


def part1(input):
    return 0


def part2(input):
    return 0


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
