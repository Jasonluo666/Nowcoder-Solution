import sys

for line in sys.stdin:
    line = line[:-1]

    if len(line) <= 8:
        print('NG')
        continue
    
    flag = {'upper': 0, 'lower': 0, 'num': 0, 'other': 0}
    for element in line:
        if 'a' <= element <= 'z':
            flag['lower'] = 1
        elif 'A' <= element <= 'Z':
            flag['upper'] = 1
        elif '0' <= element <= '9':
            flag['num'] = 1
        else:
            flag['other'] = 1
    
    if flag['upper'] + flag['lower'] + flag['num'] + flag['other'] < 3:
        print('NG')
        continue
    
    is_multiple = False
    for index in range(len(line) - 6):
        for next_index in range(index + 3, len(line) - 3):
            if line[index:index + 3] == line[next_index:next_index + 3]:
                print('NG')
                is_multiple = True
                break
        if is_multiple == True:
            break
    
    if is_multiple == False:
        print('OK')
