with open('vocabulary.txt', 'a') as v:
    eng = ""
    kor = ""
    while True:
        eng = input("영어 단어를 입력하세요: ")
        if eng == "q":
            break
        kor = input("한국어 뜻을 입력하세요: ")
        v.write("{}: {}\n".format(eng, kor))