import pygame  # pygame 모듈 가져오기
import time  # 시간 관련 모듈 가져오기
import random  # 난수 생성 모듈 가져오기

##################################
# 기본 초기화 (반드시 해야 하는 것들)

# 초기화
pygame.init()  # pygame 초기화

# 화면 크기 설정하기
width, height = 600, 600  # 화면 크기 설정
screen = pygame.display.set_mode((width, height))  # 화면 생성

# 화면 타이틀 설정
pygame.display.set_caption("Snake Game")  # 창 제목 설정
bg_color = (255, 255, 178)  # 배경 색상 설정

# FPS
clock = pygame.time.Clock()  # FPS 조정 객체 생성

#######################################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등)

# 스네이크 설정
snake_color = (255, 69, 0)  # 스네이크 색상 설정
snake_block_size = 20  # 스네이크 블록의 크기 설정
snake_speed = 15  # 스네이크의 이동 속도 설정
food_color = (255, 250, 250)  # 먹이 색상 설정
food_size = snake_block_size  # 먹이의 크기를 스네이크 블록 크기와 동일하게 설정

# 스네이크 그리기 함수
def draw_snake(snake_list):  # 스네이크 그리기 함수 정의
    for x, y in snake_list:  # 스네이크 블록 리스트의 각 블록에 대해
        pygame.draw.rect(screen, snake_color, [x, y, snake_block_size, snake_block_size])  # 스네이크 블록 그리기

# 랜덤 먹이 위치 생성 함수
def random_food_position():  # 랜덤 먹이 위치 생성 함수 정의
    x = round(random.randrange(0, width - food_size) / 20.0) * 20.0  # 랜덤 x 위치 생성
    y = round(random.randrange(0, height - food_size) / 20.0) * 20.0  # 랜덤 y 위치 생성
    return (x, y)  # 생성된 위치 반환

# 점수 표시 함수
font_style = pygame.font.SysFont(None, 35)  # 점수 표시용 폰트 설정
def display_score(score):  # 점수 표시 함수 정의
    score_text = font_style.render(f"Score : {score}", True, (0, 0, 0))  # 점수 텍스트 생성
    screen.blit(score_text, [10, 10])  # 화면에 점수 표시

# 게임 오버 메시지 함수
def game_over_message():  # 게임 오버 메시지 함수 정의
    game_over_font = pygame.font.SysFont(None, 75)  # 게임 오버 메시지 폰트 설정
    game_over_text = game_over_font.render("Game Over", True, (0, 0, 0))  # 게임 오버 텍스트 생성
    screen.blit(game_over_text, [width / 2 - 150, height / 2 - 50])  # 화면 중앙에 게임 오버 메시지 표시

# 게임 초기화 함수
def initialize_game():  # 게임 초기화 함수 정의
    global x1, y1, x1_change, y1_change, snake_list, length_of_snake, score, food_position, snake_speed  # 전역 변수 사용
    x1, y1 = width / 2, height / 2  # 스네이크의 초기 위치 설정
    x1_change, y1_change = snake_block_size, 0  # 초기 이동 방향 설정
    snake_list = []  # 스네이크 블록 리스트 초기화
    length_of_snake = 3  # 스네이크의 초기 길이 설정
    for i in range(length_of_snake):  # 스네이크 블록 추가
        snake_list.append([x1 - i * snake_block_size, y1])
    global food_position  # 전역 변수로 food_position 설정
    food_position = random_food_position()  # 초기 먹이 위치 설정
    global score, snake_speed  # 전역 변수로 score와 snake_speed 설정
    score = 0  # 초기 점수 설정
    snake_speed = 15  # 초기 스네이크 속도 설정

initialize_game()  # 게임 초기화 호출

# 이벤트 루프
running = True  # 게임이 실행 중인지 여부
game_close = False  # 게임 종료 상태
game_over = False  # 게임 오버 상태

while running:

    #################################
    # 2. 이벤트 처리 (키보드, 마우스 등)

    while game_close:  # 게임 종료 상태일 때
        screen.fill(bg_color)  # 화면 배경 색상으로 채우기
        game_over_message()  # 게임 오버 메시지 표시
        display_score(score)  # 점수 표시
        pygame.display.update()  # 화면 업데이트

        for event in pygame.event.get():  # 이벤트 처리
            if event.type == pygame.QUIT:  # 종료 이벤트
                running = False
                game_close = False
            if event.type == pygame.KEYDOWN:  # 키 입력 이벤트
                if event.key == pygame.K_q:  # 'Q' 키 눌림
                    running = False
                    game_close = False
                elif event.key == pygame.K_c:  # 'C' 키 눌림
                    initialize_game()  # 게임 초기화 호출
                    game_close = False  # 게임 종료 상태 해제

    ############################
    # 3. 게임 캐릭터 위치 정의

    for event in pygame.event.get():  # 이벤트 처리
        if event.type == pygame.QUIT:  # 종료 이벤트
            running = False
        if event.type == pygame.KEYDOWN:  # 키 입력 이벤트
            if event.key == pygame.K_LEFT and x1_change == 0:  # 왼쪽 방향키
                x1_change = -snake_block_size  # 이동 방향 변경
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change == 0:  # 오른쪽 방향키
                x1_change = snake_block_size  # 이동 방향 변경
                y1_change = 0
            elif event.key == pygame.K_UP and y1_change == 0:  # 위쪽 방향키
                y1_change = -snake_block_size  # 이동 방향 변경
                x1_change = 0
            elif event.key == pygame.K_DOWN and y1_change == 0:  # 아래쪽 방향키
                y1_change = snake_block_size  # 이동 방향 변경
                x1_change = 0

    x1 += x1_change  # 스네이크의 x 위치 업데이트
    y1 += y1_change  # 스네이크의 y 위치 업데이트
    screen.fill(bg_color)  # 화면 배경 색상으로 채우기
    pygame.draw.rect(screen, food_color, [food_position[0], food_position[1], food_size, food_size])  # 먹이 그리기
    snake_Head = [x1, y1]  # 스네이크의 머리 위치 설정
    snake_list.append(snake_Head)  # 스네이크 블록 리스트에 머리 추가

    if len(snake_list) > length_of_snake:  # 스네이크 길이가 늘어났을 때
        del snake_list[0]  # 오래된 블록 제거

    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:  # 화면 경계와 충돌 확인
        game_close = True  # 게임 종료 상태 설정

    for x in snake_list[:-1]:  # 스네이크 몸과 충돌 확인
        if x == snake_Head:
            game_close = True  # 게임 종료 상태 설정

    if x1 == food_position[0] and y1 == food_position[1]:  # 먹이와 충돌 확인
        food_position = random_food_position()  # 새로운 먹이 위치 설정
        length_of_snake += 1  # 스네이크 길이 증가
        score += 1  # 점수 증가
        snake_speed += 1  # 스네이크 속도 증가

    #################
    # 5. 화면에 그리기

    draw_snake(snake_list)  # 스네이크 그리기
    display_score(score)  # 점수 표시
    pygame.display.update()  # 화면 업데이트
    clock.tick(snake_speed)  # FPS 조정

pygame.quit()  # pygame 종료
