input_int = int(input())

count = 0
while input_int > 1:
    count += input_int % 2
    input_int = int(input_int / 2)
count += input_int

print(count)
