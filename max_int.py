
num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0

while num_int > 0:
    prev_int = num_int
    num_int = int(input("Input a number: "))
    if num_int > prev_int:
        if num_int > max_int:
            max_int = num_int

print("The maximum is", max_int)    # Do not change this line
