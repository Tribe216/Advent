from collections import defaultdict

counter = 0
coins_dict = {}
set_length_and_counter = defaultdict(int)


def load_up_coin_dict(infile):
    global coins_dict
    coins_list = []
    coins_def_dict = defaultdict()

    for line in open(infile, 'r').readlines():
        coins_list.append(int(line))
    coins_list.sort()
    coins_list.reverse()
    for i, c in enumerate(coins_list):
        coins_def_dict[i] = c
    coins_dict = dict(coins_def_dict)
    print coins_dict


def get_factors_plus_zero(num, divisor):
    if (divisor <= num):
        return [0, 1]
    else:
        return [0]


def coin_ways(rem, coin_index, running_set):
    global counter
    global all_sets

    coin_val = coins_dict[coin_index]
    coin_combos = get_factors_plus_zero(rem, coin_val)
    # print rem, coin_val, coin_combos
    for i in coin_combos:
        loop_remainder = rem - (coin_val*i)
        # print loop_remainder
        # if remainder is zero, counter++
        if i == 1:
            running_set.append(coin_val)
        if loop_remainder == 0:
            counter += 1
            set_length_and_counter[len(running_set)] += 1
            continue
        if coin_index == len(coins_dict) - 1:
            continue
        coin_ways(loop_remainder, coin_index+1, running_set[:])


load_up_coin_dict('day_17_input.txt')
coin_ways(150, 0, [])
print counter
print set_length_and_counter
