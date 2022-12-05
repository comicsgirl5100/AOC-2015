def readData(day):
    dataFile = open(f"input_files/day{day}.txt", "r")
    data = dataFile.read().split("\n")
    dataFile.close()
    return data

def readTestData(day):
    dataFile = open(f"test_input_files/day{day}.txt", "r")
    data = dataFile.read().split("\n")
    dataFile.close()
    return data