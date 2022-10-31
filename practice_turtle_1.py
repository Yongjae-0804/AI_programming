import turtle as t

t.speed(0)
t.setup(width=400, height=380) #크기설정
t.screensize( 10,10 ,'#0E639E') # 바탕색 푸른색으로 설정

def sun(r, color): # 노을의 반지름과 색을 입력
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def move(x,y): #원하는 위치로 이동
    t.pu()
    t.home()
    t.goto(x,y)
    t.pd()
    return

def mt(x,y,size,color): #산의 왼쪽 꼭지점의 위치와 크기, 색 입력
    move(x,y)
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()
    return

# 노을 그리기
move(30,20-120)
sun(180,'#9B80D8')
move(30,40-120)
sun(160, '#F383B6')
move(30,60-120)
sun(140, '#F37A76')
move(30,80-120)
sun(120, '#FE9E02')
move(30,100-120)
sun(100, '#FFC309')

#들판 그리기
move(-200,0)
t.fillcolor('#80994D')
t.begin_fill()
t.forward(400)
t.left(90)
t.forward(-190)
t.left(90)
t.forward(400)
t.end_fill()

#산 그리기
mt(-250,-80,250,'#E5F0F1')
mt(-100,-70,250,'#E5F0F1')
mt(0,-80,250,'#E5F0F1')

mt(-290,-90,200,'#CDD5D7')
mt(-150,-90,200,'#CDD5D7')
mt(-10,-85,160,'#CDD5D7')
mt(80,-90,200,'#CDD5D7')

mt(-240,-130,190,'#959C9C')
mt(-100,-110,120,'#959C9C')

#오솔길
move(105,-190)
t.color('#D4C4BE')
t.fillcolor('#D4C4BE')
t.begin_fill()
t.left(70)
t.forward(50)
t.left(30)
t.forward(20)
t.left(45)
t.forward(30)
t.left(45)
t.forward(40)

t.right(90)
t.forward(10)
t.right(90)
t.forward(40)
t.right(40)
t.forward(40)
t.right(40)
t.forward(40)
t.right(30)
t.forward(50)
t.end_fill()

#마지막 산 한개
mt(-50,-120,130,'#959C9C')

t.done()