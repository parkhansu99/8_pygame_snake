import pygame  # pygame 모듈 가져오기
import time  # 시간 관련 모듈 가져오기
import random  # 난수 생성 모듈 가져오기

# 초기화
pygame.init()  # pygame 초기화

# 화면 크기와 색상 설정
width, height = 600, 600  # 화면 크기 설정
screen = pygame.display.set_mode((width, height))  # 화면 생성
pygame.display.set_caption("Snake Game")  # 창 제목 설정
bg_color = (255, 255, 178)  # 배경 색상 설정

# 스네이크 설정
snake_color = (255, 69, 0)  # 스네이크 색상 설정
snake_block_size = 20  # 스네이크 블록의 크기 설정
snake_speed = 15  # 스네이크의 이동 속도 설정

# 스네이크 그리기 함수
def draw_snake(snake_list):  # 스네이크 그리기 함수 정의
    for x, y in snake_list:  # 스네이크 블록 리스트의 각 블록에 대해
        pygame.draw.rect(screen, snake_color, [x, y, snake_block_size, snake_block_size])  # 스네이크 블록 그리기

# 먹이 설정
food_color = (255, 250, 250)  # 먹이 색상 설정
food_size = snake_block_size  # 먹이의 크기를 스네이크 블록 크기와 동일하게 설정

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

# 게임 루프 함수
def game_loop():  # 게임 루프 함수 정의
    global snake_speed  # 전역 변수 snake_speed 사용
    game_over = False  # 게임 종료 상태 플래그 초기화
    game_close = False  # 게임 종료 화면 상태 플래그 초기화

    # 스네이크의 초기 길이를 3으로 설정
    x1, y1 = width / 2, height / 2  # 스네이크의 초기 위치 설정
    x1_change, y1_change = snake_block_size, 0  # 기본 방향을 오른쪽으로 설정
    snake_list = []  # 스네이크 블록을 저장할 리스트 초기화
    length_of_snake = 3  # 스네이크의 초기 길이 설정
    for i in range(length_of_snake):  # 초기 스네이크 블록 추가
        snake_list.append([x1 - i * snake_block_size, y1])  # 초기 스네이크 위치 설정
    clock = pygame.time.Clock()  # 게임 루프 속도를 조절하기 위한 시계 생성
    score = 0  # 점수 초기화

    food_position = random_food_position()  # 랜덤으로 먹이 위치 설정

    while not game_over:  # 게임이 종료되지 않은 동안 반복
        while game_close:  # 게임 종료 화면 상태에서
            screen.fill(bg_color)  # 배경 색상으로 화면 채우기
            game_over_message()  # 게임 오버 메시지 표시
            display_score(score)  # 점수 표시
            pygame.display.update()  # 화면 업데이트

            for event in pygame.event.get():  # 모든 이벤트를 가져와서 처리
                if event.type == pygame.QUIT:  # 이벤트 타입이 창 닫기인 경우
                    game_over = True  # 게임 종료 상태로 설정
                    game_close = False  # 게임 종료 화면 상태 플래그 해제
                if event.type == pygame.KEYDOWN:  # 이벤트 타입이 키보드 키 눌림인 경우
                    if event.key == pygame.K_q:  # 'Q' 키가 눌린 경우
                        game_over = True  # 게임 종료 상태로 설정
                        game_close = False  # 게임 종료 화면 상태 플래그 해제
                    elif event.key == pygame.K_c:  # 'C' 키가 눌린 경우
                        game_loop()  # 게임 루프 다시 시작
                        return  # 현재 게임 루프 종료

        for event in pygame.event.get():  # 모든 이벤트를 가져와서 처리
            if event.type == pygame.QUIT:  # 이벤트 타입이 창 닫기인 경우
                game_over = True  # 게임 종료 상태로 설정
            if event.type == pygame.KEYDOWN:  # 이벤트 타입이 키보드 키 눌림인 경우
                if event.key == pygame.K_LEFT and x1_change == 0:  # 왼쪽 화살표 키가 눌린 경우
                    x1_change = -snake_block_size  # x 좌표 이동값을 음수로 설정
                    y1_change = 0  # y 좌표 이동값은 변화 없음
                elif event.key == pygame.K_RIGHT and x1_change == 0:  # 오른쪽 화살표 키가 눌린 경우
                    x1_change = snake_block_size  # x 좌표 이동값을 양수로 설정
                    y1_change = 0  # y 좌표 이동값은 변화 없음
                elif event.key == pygame.K_UP and y1_change == 0:  # 위쪽 화살표 키가 눌린 경우
                    y1_change = -snake_block_size  # y 좌표 이동값을 음수로 설정
                    x1_change = 0  # x 좌표 이동값은 변화 없음
                elif event.key == pygame.K_DOWN and y1_change == 0:  # 아래쪽 화살표 키가 눌린 경우
                    y1_change = snake_block_size  # y 좌표 이동값을 양수로 설정
                    x1_change = 0  # x 좌표 이동값은 변화 없음

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:  # 벽에 닿으면 게임 종료
            game_close = True  # 게임 종료 화면 상태로 설정

        x1 += x1_change  # x 좌표 업데이트
        y1 += y1_change  # y 좌표 업데이트
        screen.fill(bg_color)  # 배경 색상으로 화면 채우기
        pygame.draw.rect(screen, food_color, [food_position[0], food_position[1], food_size, food_size])  # 먹이 그리기
        snake_Head = [x1, y1]  # 스네이크 머리 위치 저장
        snake_list.append(snake_Head)  # 스네이크 리스트에 머리 추가
        if len(snake_list) > length_of_snake:  # 스네이크 길이 초과 시 가장 오래된 블록 삭제
            del snake_list[0]

        for x in snake_list[:-1]:  # 스네이크 몸통에 닿은 경우 게임 종료
            if x == snake_Head:  # 스네이크 머리와 몸통의 위치가 같을 경우
                game_close = True  # 게임 종료 화면 상태로 설정

        draw_snake(snake_list)  # 스네이크 그리기
        display_score(score)  # 점수 표시

        pygame.display.update()  # 화면 업데이트

        if x1 == food_position[0] and y1 == food_position[1]:  # 스네이크가 먹이를 먹었을 때
            food_position = random_food_position()  # 새 위치로 먹이 이동
            length_of_snake += 1  # 스네이크 길이 증가
            score += 1  # 점수 증가
            snake_speed += 1  # 스피드 증가

        clock.tick(snake_speed)  # 게임 루프 속도 조절

    pygame.quit()  # pygame 종료
    quit()  # 프로그램 종료

game_loop()  # 게임 루프 함수 호출
