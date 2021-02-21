import webbrowser

filePath = "IDON'TKNOW"
attached = False

menu = '''
a. 카톡 파일 연결하기
b. 대화 분석하기
c. 사용법
d. 나가기

> '''

analyze_menu = '''
a. 누가누가 가장 채팅을 많이 했을까
b. 이 친구는 얼마나 많이 채팅 했을까
c. 특정 단어가 얼마나 나왔을까
d. 특정 단어를 가장 많이 사용한 친구는 누구일까
e. 이 친구가 한 말들만 모아서 보자
f. 사진을 가장 많이 보낸 친구는 누구일까

> '''

def attach():
    global filePath, attached
    choice = input("a. 절대좌표로 연결하기 \nb. 상대좌표로 연결하기 \n \n> ")
    if choice == 'a':
        path = input('절대좌표: ')
        if path[-4:] == '.txt':
            filePath = path
            print(filePath + "에 있는 텍스트 파일과 연결되었습니다.")
            attached = True
            return
        else:
            print("텍스트 파일을 연결해주세요.")
            attach()
    elif choice == 'b':
        path = input('상대좌표: ')
        if path[-4:-1] == '.txt':
            filePath = open(path)
            print(filePath + "에 있는 텍스트 파일과 연결되었습니다.")
            attached = True
            return
        else:
            print("텍스트 파일을 연결해주세요.")
            attach()
    else:
        print("유효하지 않은 선택 입니다.")
        attach()


def analyze():
    global attached
    print('-'*40)
    if attached == True:
        choice = input(analyze_menu)
        if choice.lower() == 'a':
            showMostChatPerson()
        elif choice.lower() == 'b':
            countPersonChat()
        elif choice.lower() == 'c':
            countParicularWord()
        elif choice.lower() == 'd':
            showMostParticularWordPerson()
        elif choice.lower() == 'e':
            showAllParticularPersonChat()
        elif choice.lower() == 'f':
            showMostPhotoPerson()
        else:
            print("유효하지 않은 선택 입니다.")
            analyze()
    else:
        print("먼저 대화 파일과 연결해주세요")
        attach()

def showMostChatPerson():
    global filePath

    print('-'*40)

    people = {}

    file = open(filePath, 'r', encoding='utf-8')
    while True:
        line = file.readline()
        if not line:
            file.close()
            break
        if len(line) > 25:
            words = line.split()
            if '년' in words[0] and words[0][0] == '2': #C:/Users/USER/Desktop/KakaoTalkChats.txt
                if not words[5][-1] == '이' and not words[5] == '삭제된':
                    if words[5] in people.keys():
                        people[words[5]] += 1
                    else:
                        people[words[5]] = 1

    print({k: v for k, v in sorted(people.items(), key=lambda item: item[1])})

def countPersonChat():
    global filePath

    print('-'*40)

    count = 0

    name = input('누구?: ')

    file = open(filePath, 'r', encoding='utf-8')
    while True:
        line = file.readline()
        if not line:
            file.close()
            break
        if len(line) > 25:
            words = line.split()
            if '년' in words[0] and words[0][0] == '2':
                if not words[-5][-1] == '이':
                    if name in words[5]:
                        count+=1
    print("{}(이)는 {}번 채팅을 했습니다".format(name, count))


def countParicularWord():
    global filePath

    print('-'*40)

    count = 0

    word = input('무슨 단어?: ')

    file = open(filePath, 'r', encoding='utf-8')
    while True:
        line = file.readline()
        if not line:
            file.close()
            break
        if len(line) > 25:
            words = line.split()
            if '년' in words[0] and words[0][0] == '2':
                if not words[-5][-1] == '이':
                    if word in words[7:]:
                        count+=1
    print("{}은 {}번 나왔습니다".format(word, count))


def showMostParticularWordPerson():
    global filePath

    print('-'*40)

    people = {}

    word = input('무슨 단어?: ')

    file = open(filePath, 'r', encoding='utf-8')
    while True:
        line = file.readline()
        if not line:
            file.close()
            break
        if len(line) > 25:
            words = line.split()
            if '년' in words[0] and words[0][0] == '2':
                if not words[-5][-1] == '이':
                    if word in words[7:]:
                        if words[5] in people.keys():
                            people[words[5]] += 1
                        else:
                            people[words[5]] = 1
    print({k: v for k, v in sorted(people.items(), key=lambda item: item[1])})


def showAllParticularPersonChat():
    global filePath

    print('-'*40)

    name = input('누구?: ')

    file = open(filePath, 'r', encoding='utf-8')
    while True:
        line = file.readline()
        if not line:
            file.close()
            break
        if len(line) > 25:
            words = line.split()
            if '년' in words[0] and words[0][0] == '2':
                if not words[-5][-1] == '이':
                    if name in words[5]:
                        for i in words[7:]:
                            print(i, end=' ')
                        print('\n')

def showMostPhotoPerson():
    global filePath

    print('-'*40)

    people = {}

    file = open(filePath, 'r', encoding='utf-8')
    while True:
        line = file.readline()
        if not line:
            file.close()
            break
        if len(line) > 25:
            words = line.split()
            if '년' in words[0] and words[0][0] == '2':
                if not words[-5][-1] == '이':
                    if words[-1][-4:] in ['.png','.jpg']:
                        if words[5] in people.keys():
                            people[words[5]] += 1
                        else:
                            people[words[5]] = 1
    print({k: v for k, v in sorted(people.items(), key=lambda item: item[1])})

def instruct():
    print('-'*40)
    url = 'C:/Users/USER/Desktop/instructions/instruction.html'
    webbrowser.open(url)



##########################################################################################

if __name__ == "__main__":
    while True:
        print('-'*40)
        choice = input(menu)
        if choice == 'a':
            attach()
        elif choice == 'b':
            analyze()
        elif choice == 'c':
            instruct()
        elif choice == 'd':
            exit()
