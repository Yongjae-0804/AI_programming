# 파일 입력 받기
f = open('KWU-AI-Programming\Homework\hw2_2019741045\Data.csv', 'r',encoding= 'utf-8') #인코딩 필수
tmp1 = f.read()
f.close()
tmp1 = tmp1[1:] #첫 공백문자 제거

tmp2 = tmp1.split('\n') #개행문자 기준으로 1차원 리스트만들기
                        #스플릿은 인자를 기준으로 나눠 준다.
data=[] #데이타 리스트

for i in tmp2: # 콤마를 기준으로 2차원 리스트 만들기
    data.append(i.split(','))

del data[-1] #데이타의 마지막 공백문자 제거
inform_cal = data.pop(0) #후일 비교를 위해 데이타의 첫번째 열을 정보칼럼으로 해주고 데이타에서 삭제

# 데이타의 행혈의 크기 구해놓기
len_row = len(data)
len_cal = len(inform_cal)

name_row = []
for i in range(len_row):
    name_row.append(data[i][0])

def name(Name):
    if Name not in name_row:
        print('이름이 없네요 다시!')
        return

    n = name_row.index(Name) #해당하는 이름을 찾아 몇번째 열에있는지 알나낸다.

    for i in range(len_cal):
        print('{:>5}'.format(inform_cal[i]), end=" ") #출력을 5칸 좌측 정렬 프린트문 끝날땐 개행문자 말고 공백
    print()

    for i in range(len_cal):
        print('{:>5}'.format(data[n][i]), end= " ")
    print()

    return

def name_score(Name,Score):
    if Name not in name_row:
        print('이름이 없네요 다시!')
        return 0
    n = name_row.index(Name)

    if Score not in inform_cal:
        print('해당하는 점수가 없네요 다시!')
        return 0
    s = inform_cal.index(Score)
    print(data[n][s])

def score(Score):
    if Score not in inform_cal:
        print('해당하는 점수가 없네요 다시!')
        return
    s = inform_cal.index(Score)

    dic_data = {}
    for i in range(len_row):
        dic_data[name_row[i]] = data[i][s]
    dic_data
    
    print('{:>7}{:>5}'.format(inform_cal[0],inform_cal[s]))
    for i in sorted(dic_data):
        if len(i)==5:
            print('{}{:>5}'.format(i, dic_data[i]))
        else:
            print('{:>7}{:>5}'.format(i, dic_data[i]))

read_me = """
원하시는 수행의 번호를 입력하세요
1. 선수의 이름을 입력하시면 세부 항목을 출력합니다.
2. 선수의 이름과 항목을 입력하시면 그 값을 출력합니다.
3. 항목이름을 입력하시면 모든 선수의 항목을 출력합니다.(선수이름 내림차순)
4. 프로그램을 종료합니다.
"""
q = int(input(read_me))
while(1):
    if q == 1:
        Name = input('선수 이름을 입력하세요: ')
        name(Name)
    elif q == 2:
        Name = input('선수 이름을 입력하세요: ')
        Score = input('항목을 입력하세요: ')
        name_score(Name, Score)
    elif q == 3:
        Score = input('항목을 입력하세요: ')
        score(Score)
    elif q == 4:
        break
    else:
        print('1~4 의 숫자만 다시 입력하세요')
        print(read_me)
    q = int(input('원하시는 수행의 번호를 입력하세요: '))

