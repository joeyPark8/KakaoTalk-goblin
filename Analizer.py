import os
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
    saveFile = open("save/saveFile.txt", 'r')

    line = saveFile.readline()

    if line == '':
        filePath = input('파일 이름을 입력해 주세요: ')
        if filePath[-4:] == '.txt':
            attached = True
            print(filePath + ' 파일과 연결되었습니다.')
            save(filePath)
            return
        else:
            print('파일 이름 또는 파일 확장자가 잘못되었습니다')
            return

    saveFile.close()

    reply = input("{} 파일로 계속 하시겠습니까?(y/n) ".format(line)).lower()
    if reply == 'y':
        filePath = line
        attached = True
        print(filePath + ' 파일과 연결되었습니다.')
        return
    elif reply == 'n':
        filePath = input('파일 이름을 입력해 주세요: ')
        if filePath[-4:] == '.txt':
            attached = True
            print(filePath + ' 파일과 연결되었습니다.')
            save(filePath)
            return
        else:
            print('파일 이름 또는 파일 확장자가 잘못되었습니다')
            return
    else:
        print('유효하지 않은 선택입니다')
        return


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

    file = open('files/' + filePath, 'r', encoding='utf-8')
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

    file = open('files/' + filePath, 'r', encoding='utf-8')
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

    file = open('files/' + filePath, 'r', encoding='utf-8')
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

    file = open('files/' + filePath, 'r', encoding='utf-8')
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

    file = open('files/' + filePath, 'r', encoding='utf-8')
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

    file = open('files/' + filePath, 'r', encoding='utf-8')
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
    try:
        from urllib import pathname2url
    except:
        from urllib.request import pathname2url

    print('-'*40)
    url = 'file:{}'.format(pathname2url(os.path.abspath('instructions/instruction.html')))
    webbrowser.open(url)


def save(path):
    saveFile = open("save/saveFile.txt", 'w')
    saveFile.write(path)
    saveFile.close()

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
