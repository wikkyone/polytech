N = int(input())
if N > 1:
    for i in range(2, N):
        if N % i == 0:
            print("Число не является простым")
            break
        i += 1
    else:
        print("Число является простым")
# делаем второй else, тк по условию простое число - это число, которое больше 1
else:
    print("Число не является простым")
