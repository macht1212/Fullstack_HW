print("Числа Фибоначи\n")

N = int(input("Сколько чисел вывести "))
print()
count_fir = 0
count_sec = 1

count = [1]


def fibo(N):
    global count_fir
    global count_sec
    for i in range(0, N):
        count_fir += count_sec
        count.append(count_fir)
        count_sec = count_sec + count_fir
        count.append(count_sec)


fibo(int(N / 2)) if N % 2 == 0 else (fibo(int(N // 2)),
                                     count_fir == count_fir + count_sec,
                                     count.append(count_fir))


print(count)
