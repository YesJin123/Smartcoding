import random

random_number = random.randint(1, 100)

# print(random_number)
count = 1

while True:
    try : 
        my_number = int(input("1부터 100 사이의 숫자를 입력하세요 "))

        if my_number > random_number : 
            print("DOWN")
        elif my_number < random_number :
            print("UP")
        elif my_number == random_number :
            print(f"축하드립니다!! {count} 만에 맞추셨습니다")
            break

        count = count + 1

    except: print("숫자로 입력하세요")