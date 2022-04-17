def el_num(line, type=int, num_r=''):
    num_list = []
    num = num_r
    # for line in f_file:
    for char in line:
        if char.isdigit():
            num = num + char
        else:
            if num != num_r:
                num_list.append(type(num))
                num = num_r
    if num != num_r:
        num_list.append(type(num))
    return num_list
