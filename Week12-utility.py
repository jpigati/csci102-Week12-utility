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
def ScoreFinder(players, scores, person):
    score = False
    for i in range(len(players)):
        if players[i].lower() == person.lower():
            score = scores[i]
    if score == False:
        print('OUTPUT player not found')
    else:
        print('OUTPUT', person, 'got a score of', score)
def Union(lista, listb):
    final_list = []
    for i in lista:
        if i not in final_list:
            final_list.append(i)
    for i in listb:
        if i not in final_list:
            final_list.append(i)
    return final_list
