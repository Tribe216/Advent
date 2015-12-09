#!/usr/bin/python

main_dict = {}
global_ops = 0

commands = open('day_7_input_p2.txt', 'r').readlines()
for line in commands:
    line_elem = line.rstrip().split(' ')
    target = line_elem[-1]
    r_part = line_elem[-3]
    if len(line_elem) > 3:
        operator = line_elem[-4]
    else:
        operator = ''
    if len(line_elem) > 4:
        l_part = line_elem[-5]
    else:
        l_part = ''

    # print target, '=', l_part, operator, r_part

    main_dict[target] = {
        'target': target,
        'l_part': l_part,
        'r_part': r_part,
        'operator': operator,
        'num_value' : None
    }

def evaluate(elem):
    global global_ops
    global_ops += 1
    # print type(elem)
    print global_ops, "currently on: ", elem['target'], '=', elem['l_part'], elem['operator'], elem['r_part'], 'numvalue', elem['num_value']
    # when no operator, return r part integer

    if elem['num_value']:
        return int(elem['num_value'])

    if elem['operator'] == '':
        if elem['r_part'].isdigit():
            elem['num_value'] = int(elem['r_part'])
        else:
            elem['num_value'] =  int(evaluate(main_dict[elem['r_part']]))
        return elem['num_value']

    # when not, return bit complement of element referenced by r_part
    if elem['operator'] == 'NOT':
        if elem['r_part'].isdigit():
            elem['num_value'] = ~int(elem['r_part'])
        else:
            elem['num_value'] = ~int(evaluate(main_dict[elem['r_part']]))
        return elem['num_value']

    # when AND, return l_part AND r_part
    if elem['operator'] == 'AND':
        if elem['l_part'].isdigit() and elem['r_part'].isdigit():
            elem['num_value'] = int(elem['l_part']) & int(elem['r_part'])

        elif elem['l_part'].isdigit() and not elem['r_part'].isdigit():
            elem['num_value'] = int(elem['l_part']) & int(evaluate(main_dict[elem['r_part']]))

        elif not elem['l_part'].isdigit() and elem['r_part'].isdigit():
            elem['num_value'] = int(evaluate(main_dict[elem['l_part']])) & int(elem['r_part'])

        else:
            elem['num_value'] = int(evaluate(main_dict[elem['l_part']])) & int(evaluate(main_dict[elem['r_part']]))

        return elem['num_value']

    # when OR, return l_part OR r_part
    if elem['operator'] == 'OR':

        if elem['l_part'].isdigit() and elem['r_part'].isdigit():
            elem['num_value'] = int(elem['l_part']) | int(elem['r_part'])

        elif elem['l_part'].isdigit() and not elem['r_part'].isdigit():
            elem['num_value'] = int(elem['l_part']) | int(evaluate(main_dict[elem['r_part']]))

        elif not elem['l_part'].isdigit() and elem['r_part'].isdigit():
            elem['num_value'] = int(evaluate(main_dict[elem['l_part']])) | int(elem['r_part'])

        else:
            elem['num_value'] = int(evaluate(main_dict[elem['l_part']])) | int(evaluate(main_dict[elem['r_part']]))
            
        return elem['num_value']

    # lshift
    if elem['operator'] == 'LSHIFT':
        elem['num_value'] = int(evaluate(main_dict[elem['l_part']])) << int(elem['r_part'])
        return elem['num_value']

    # rshift
    if elem['operator'] == 'RSHIFT':
        elem['num_value'] = int(evaluate(main_dict[elem['l_part']])) >> int(elem['r_part'])
        return elem['num_value']

answer = evaluate(main_dict['a'])

print main_dict['a']
#print answer, global_ops
