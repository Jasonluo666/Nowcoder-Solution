import sys

table = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E':0, 'wrong': 0, 'private': 0}
verify_list = [254, 252, 248, 240, 224, 192, 128, 0]
for line in sys.stdin:
    ip, mask = line.split('~')
    mask = mask[:-1]
    valid_flag = True

    for element in ip.split('.'):
        if int(element) >255 or int(element) < 0:
            valid_flag = False
    for element in mask.split('.'):
        if int(element) >255 or int(element) < 0:
            valid_flag = False
    
    if valid_flag == True:
        separated_mask = mask.split('.')
        if len(separated_mask) == 4 and separated_mask[0].isdigit() and separated_mask[1].isdigit() and separated_mask[2].isdigit() and separated_mask[3].isdigit():
            full_size = True
            for element in separated_mask:
                element = int(element)
                
                if full_size == True and element < 255:
                    full_size = False
                    if element not in verify_list:
                        valid_flag = False
                if full_size == False and element != 0:
                    valid_flag = False
        else:
            valid_flag = False
    
    if valid_flag == True:
        separated_ip = ip.split('.')
        if len(separated_ip) == 4 and separated_ip[0].isdigit() and separated_ip[1].isdigit() and separated_ip[2].isdigit() and separated_ip[3].isdigit():
            if valid_flag == True:
                first_part, second_part = int(separated_ip[0]), int(separated_ip[1])

                if first_part == 10 or (first_part == 172 and 16 <= second_part <= 31) or (first_part == 192 and second_part == 168):
                    table['private'] += 1
                
                if 1 <= first_part <= 126:
                    table['A'] += 1
                elif 128 <= first_part <= 191:
                    table['B'] += 1
                elif 192 <= first_part <= 223:
                    table['C'] += 1
                elif 224 <= first_part <= 239:
                    table['D'] += 1
                elif 240 <= first_part <= 255:
                    table['E'] += 1
        else:
            valid_flag = False
    
    if valid_flag == False:
        table['wrong'] += 1

print(str(table['A']) + ' ' + str(table['B']) + ' ' + str(table['C']) + ' ' + str(table['D']) + ' ' + str(table['E']) + ' ' + str(table['wrong']) + ' ' + str(table['private']))