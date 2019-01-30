import sys

for line in sys.stdin:
    hex_num = (line[2:-1]).lower()
    num = 0
    for index in range(len(hex_num)):
        base = 16 ** index
        times = None

        if '0' <= hex_num[-(index + 1)] <= '9':
            times = int(hex_num[-(index + 1)])
        else:
            times = ord(hex_num[-(index + 1)]) - ord('a') + 10
        num += base * times   
    print(num)