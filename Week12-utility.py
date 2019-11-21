def PrintOutput(output):
    print('OUTPUT', output)
def LoadFile(filename):
    with open(filename) as file:
        lines = file.read().split()
        return lines
def UpdateString(string, string_add, index): #doesnt replace just adds
    return string[:index] + string_add + string[(index+1):]
def FindWordCount(List, string):
    count = List.count(string)
    return count
