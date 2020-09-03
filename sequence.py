n = int(input("Enter the length of the sequence: ")) # Do not change this line
count = 1
num_int = 3
num2_int = 2
num3_int = 1

if n == 1:
    print(num3_int)
elif n == 2:
    print(num3_int)
    print(num2_int)
elif n == 3:
    print(num3_int)
    print(num2_int)
    print(num_int)
elif n > 3:
    print(num3_int)
    print(num2_int)
    print(num_int)
    while count <= n:
        sum_int = num_int + num2_int + num3_int
        num3_int = num2_int
        num2_int = num_int
        num_int = sum_int
        count += 1
        print(sum_int)