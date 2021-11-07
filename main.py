from random import randint

def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []

    while len(new_guess) < 3:
        enter = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))
        if 0 <= enter <= 9 and enter not in new_guess:
            new_guess.append(enter)
        elif enter in new_guess:
            print("중복되는 값입니다. 다시 입력하세요")
        else:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")

    return new_guess


def get_score(guess,answer):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i] == answer[i]:
            strike_count += 1
        elif guess[i] in answer:
            ball_count += 1

    return strike_count, ball_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0
print("0과 9사이의 서로 다른 숫자x 3개를 랜덤한 순서로 뽑았습니다.\n")

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    if s == 3:
        print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
        break
    else:
        print("{}S {}B\n".format(s, b))
        tries += 1