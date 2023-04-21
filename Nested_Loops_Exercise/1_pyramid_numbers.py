size = int(input())
counter = 0

for row in range(1, size + 1):  #1
    for col in range(1, row + 1):  #1, 2   => 1 iteraciq
        counter += 1

        print(counter, end=" ") if row != col else print(counter)

        if counter == size:
            exit()
