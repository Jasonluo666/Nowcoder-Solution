input_num = int(input())

prime_list = []
init_prime = 2
while input_num != 1:
    if input_num % init_prime == 0:
        input_num /= init_prime
        prime_list.append(init_prime)
        init_prime = 2
    else:
        init_prime += 1

print(' '.join([str(x) for x in prime_list]) + ' ')