def PrintOutput(output):
    print('OUTPUT', output)
def LoadFile(filename):
    with open(filename) as file:
        lines = file.read().split()
        return lines
