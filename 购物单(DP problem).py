# 0-1背包问题

# price limitation, item number
total_price, item_num = input().split(' ')
total_price = int(total_price)
item_num = int(item_num)

# item contains 0-2 attachemt(s)
price_list = [[0, 0, 0]]
value_list = [[0, 0, 0]]
# track the item position
index_list = [0]

# input the item info -> price, importance
for _ in range(item_num):
    price, importance, is_attachment = input().split(' ')
    price, importance, is_attachment = int(price), int(importance), int(is_attachment)

    # main
    if is_attachment == 0:
        price_list.append([price, 0, 0])
        value_list.append([price * importance, 0, 0])

        index_list.append(len(price_list) - 1)
    else:
        # first attachment
        if price_list[index_list[is_attachment]][1] == 0:
            price_list[index_list[is_attachment]][1] = price
            value_list[index_list[is_attachment]][1] = price * importance
        # second attachment
        else:
            price_list[index_list[is_attachment]][2] = price
            value_list[index_list[is_attachment]][2] = price * importance
        index_list.append(None)

'''
    DP table -> cache -> reduce the computational cost
        
        formula: table[item][remain weight] = max{table[item - 1][remain weight], table[item - 1][remain weight - item weight] + item value}  
        
        P.S. from first item to the last, consider both situations where the ith item is and isn't included
'''
dp_table = [[0 for x in range(32000)] for x in range(60)]
for item in range(1, len(price_list)):
    for remain_price in range(total_price, 0, -1):
        # only main -> add dp_table[item][remain_price] to track the maxmum current value
        if remain_price >= price_list[item][0]:
            dp_table[item][remain_price] = max(dp_table[item][remain_price], dp_table[item - 1][remain_price], dp_table[item - 1][remain_price - price_list[item][0]] + value_list[item][0])
        # main + 1st
        if remain_price >= price_list[item][0] + price_list[item][1]:
            dp_table[item][remain_price] = max(dp_table[item][remain_price], dp_table[item - 1][remain_price], dp_table[item - 1][remain_price - price_list[item][0] - price_list[item][1]] + value_list[item][0] + value_list[item][1])
        # main + 2rd
        if remain_price >= price_list[item][0] + price_list[item][2]:
            dp_table[item][remain_price] = max(dp_table[item][remain_price], dp_table[item - 1][remain_price], dp_table[item - 1][remain_price - price_list[item][0] - price_list[item][2]] + value_list[item][0] + value_list[item][2])
        # main + 1st + 2rd
        if remain_price >= price_list[item][0] + price_list[item][1] + price_list[item][2]:
            dp_table[item][remain_price] = max(dp_table[item][remain_price], dp_table[item - 1][remain_price], dp_table[item - 1][remain_price - price_list[item][0] - price_list[item][1] - price_list[item][2]] + value_list[item][0] + value_list[item][1] + value_list[item][2])

print(dp_table[len(price_list) - 1][total_price])
