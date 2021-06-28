with open('vocabulary.txt', 'r') as v:
    for line in v:
        voca = line.strip().split(": ")
        answer = input("{}: ".format(voca[1]))
        if answer == voca[0]:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(voca[0]))