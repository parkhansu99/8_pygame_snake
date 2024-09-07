from turtle import Turtle, Screen
import time
import random

### 스크린 만들기

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("khaki")
screen.title("Snake Game")
screen.tracer(0)

### 방향키에 따른 방향 전환 : 이동을 직접 (X), 방향 선회만 (O)

def up():
    if snakes[0].heading() != 270: # 아래쪽이 아닐 때만
        snakes[0].setheading(90) # 위쪽으로 이동
def down():
    if snakes[0].heading() != 90: # 위쪽이 아닐 때만
        snakes[0].setheading(270) # 아래쪽으로 이동
def right():
    if snakes[0].heading() != 180: # 왼쪽이 아닐 때만
        snakes[0].setheading(0) # 오른쪽으로 이동
def left():
    if snakes[0].heading() != 0: # 오른쪽이 아닐 때만
        snakes[0].setheading(180) # 왼쪽으로 이동

screen.listen()
screen.onkeypress(up, 'Up') 
screen.onkeypress(down, 'Down')
screen.onkeypress(right, 'Right')
screen.onkeypress(left, 'Left') # 대문자로 사용해야 함

### 스네이크 생성

def create_snake(pos):
    snake_body = Turtle()
    snake_body.shape("square")
    snake_body.color("orangered")
    snake_body.up()
    snake_body.goto(pos)
    snakes.append(snake_body) # 스네이크 길이를 길게 만듦

start_pos = [(0, 0), (-20, 0), (-40, 0)]
snakes = []

for pos in start_pos:
    create_snake(pos)

### 먹이 만들기

def rand_pos():
    rand_x = random.randint(-250, 250)
    rand_y = random.randint(-250, 250)
    return rand_x, rand_y

food = Turtle()
food.shape("circle")
food.color("snow")
food.up()
food.speed(0)
food.goto(rand_pos())

### 점수 표시

score = 0

def score_update():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f"점수 : {score}", font = ("", 15, "bold"))

score_pen = Turtle()
score_pen.ht()
score_pen.up()
score_pen.goto(-270, 250)
score_pen.write(f"점수 : {score}", font = ("", 15, "bold"))

### 게임 오버

def game_over():
    score_pen.goto(0, 0)
    score_pen.write("Game Over", False, "center", ("", 30, "bold"))

### 자동으로 앞을 향해 가도록 하기 (아래에는 코드가 없도록 하기)

game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)

    for i in range(len(snakes) -1, 0, -1):
        snakes[i].goto(snakes[i-1].pos())
    snakes[0].forward(20) # 게임 속도

    # 스네이크의 머리가 먹이와 부딪힌 경우
    if snakes[0].distance(food) < 15: 
        score_update()
        food.goto(rand_pos())
        create_snake(snakes[-1].pos())

    # 벽에 닿아도 게임 종료
    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 or snakes[0].ycor() > 280 or snakes[0].ycor() <-280:
        game_on = False
        game_over()

    # 자기 몸통에 닿아도 게임 종료
    for body in snakes[1:]: # 머리 이외에 다른 것이 닿은 경우
        if snakes[0].distance(body) < 10:
            game_on = False
            game_over()

screen.mainloop()  # 이벤트 루프를 유지하여 창이 닫히지 않도록 함