import copy


def all_in_one():
    
    data = [
        [6, 8, 8],
        [2, 8, 8],
        [5, 5, 5],
    ]

    origin_data = copy.deepcopy(data)
    # 按键记录器
    recorder = []
    print('==========原始数据==========')
    for row in origin_data:
        print('{}\t{}\t{}'.format(*row))
    print('\n')


    # 方案1
    # step_one(data, recorder)
    # step_two(data, recorder)
    # step_three(data, recorder)
    # step_four(data, recorder)
    
    # 方案2
    step_one_v2(data, recorder)
    print('==========执行完步骤1_v2的结果==========')
    for row in data:
        print('{}\t{}\t{}'.format(*row))
    step_two_v2(data, recorder)
    
    
    print('==========最终数据==========')
    for row in data:
        print('{}\t{}\t{}'.format(*row))
    print('\n')
    print('==========按钮步骤==========')
    print('共{}步: {}'.format(
        len(recorder),
        '==>'.join(recorder))
    )

def push_10(data, recorder):
    """
    按10键
    """
    data[1][0] = get_value(data[1][0], 1)
    data[0][0] = get_value(data[0][0], 1)
    data[1][1] = get_value(data[1][1], 1)
    data[2][0] = get_value(data[2][0], 1)

    recorder.append('10键')


def push_12(data, recorder):
    """
    按12键
    """
    data[1][2] = get_value(data[1][2], 1)
    data[0][2] = get_value(data[0][2], 1)
    data[1][1] = get_value(data[1][1], 1)
    data[2][2] = get_value(data[2][2], 1)

    recorder.append('12键')


def push_21(data, recorder):
    """
    按21键
    """
    data[2][1] = get_value(data[2][1], 1)
    data[2][0] = get_value(data[2][0], 1)
    data[1][1] = get_value(data[1][1], 1)
    data[2][2] = get_value(data[2][2], 1)

    recorder.append('21键')


def push_20(data, recorder):
    """
    按20键
    """
    data[2][0] = get_value(data[2][0], 1)
    data[1][0] = get_value(data[1][0], 1)
    data[2][1] = get_value(data[2][1], 1)

    recorder.append('20键')


def push_02(data, recorder):
    """
    按02键
    """
    data[0][2] = get_value(data[0][2], 1)
    data[0][1] = get_value(data[0][1], 1)
    data[1][2] = get_value(data[1][2], 1)

    recorder.append('20键')


def push_22(data, recorder):
    """
    按22键
    """
    data[2][2] = get_value(data[2][2], 1)
    data[2][1] = get_value(data[2][1], 1)
    data[1][2] = get_value(data[1][2], 1)

    recorder.append('22键')


def push_01(data, recorder):
    """
    按01键
    """
    data[0][1] = get_value(data[0][1], 1)
    data[0][0] = get_value(data[0][0], 1)
    data[1][1] = get_value(data[1][1], 1)
    data[0][2] = get_value(data[0][2], 1)

    recorder.append('01键')


def push_00(data, recorder):
    """
    按00键
    """
    data[0][0] = get_value(data[0][0], 1)
    data[1][0] = get_value(data[1][0], 1)
    data[0][1] = get_value(data[0][1], 1)

    recorder.append('00键')


def push_12(data, recorder):
    """
    按12键
    """
    data[1][2] = get_value(data[1][2], 1)
    data[0][2] = get_value(data[0][2], 1)
    data[1][1] = get_value(data[1][1], 1)
    data[2][2] = get_value(data[2][2], 1)

    recorder.append('12键')


def push_11(data, recorder):
    """
    按11键
    """
    data[1][1] = get_value(data[1][1], 1)
    data[0][1] = get_value(data[0][1], 1)
    data[1][0] = get_value(data[1][0], 1)
    data[1][2] = get_value(data[1][2], 1)
    data[2][1] = get_value(data[2][1], 1)

    recorder.append('11键')


def step_one(data, recorder):

    # 按10键， 使10键与01键相同
    step_10_to_01 = diff(data[1][0], data[0][1])
    for _ in range(step_10_to_01):
        push_10(data, recorder)

    # 按12键， 使12键与01键相同
    step_12_to_01 = diff(data[1][2], data[0][1])
    for _ in range(step_12_to_01):
        push_12(data, recorder)

    # 按21键， 使21键与01键相同
    step_21_to_01 = diff(data[2][1], data[0][1])
    for _ in range(step_21_to_01):
        push_21(data, recorder)


def step_two(data, recorder):

    # 使20键与02键相同
    if data[2][0] != data[0][2]:
        while True:
            # 按了20键
            push_20(data, recorder)
            # 按了01键
            push_01(data, recorder)
            # 按了12键
            push_12(data, recorder)

            if data[2][0] == data[0][2]:
                break

    # 使22键与00键相同
    if data[2][2] != data[0][0]:
        while True:
            # 按了22键
            push_22(data, recorder)
            # 按了10键
            push_10(data, recorder)
            # 按了01键
            push_01(data, recorder)

            if data[2][2] == data[0][0]:
                break


def step_three(data, recorder):

    # 使00键, 02键, 20键, 22键相同
    if data[0][0] != data[0][2] or data[0][0] != data[2][0] \
            or data[0][0] != data[2][2]:
        while True:
            # 按20键
            push_20(data, recorder)
            # 按02键
            push_02(data, recorder)

            if data[0][0] == data[0][2] and data[0][0] == data[2][0] \
                    and data[0][0] == data[2][2]:
                break


def step_four(data, recorder):

    # 使11键, 00键, 02键, 20键, 22键相同
    if data[1][1] != data[0][0] or data[1][1] != data[0][2] \
            or data[1][1] != data[2][0] or data[1][1] != data[2][2]:
        while True:
            # 按11键
            push_11(data, recorder)

            if data[1][1] == data[0][0] and data[1][1] == data[2][0] \
                    and data[1][1] == data[2][0] and data[1][1] == data[2][2]:
                break

    # 使11键, 01键, 10键, 12键, 21键相同
    if data[1][1] != data[0][1] or data[1][1] != data[1][0] \
            or data[1][1] != data[1][2] or data[1][1] != data[2][1]:
        while True:
            # 按00键
            push_00(data, recorder)
            # 按02键
            push_02(data, recorder)
            # 按20键
            push_20(data, recorder)
            # 按22键
            push_22(data, recorder)
            # 按11键
            push_11(data, recorder)

            if data[1][1] == data[0][1] and data[1][1] == data[1][0] \
                    and data[1][1] == data[1][2] and data[1][1] == data[2][1]:
                break

            # if (data[1][1] + data[1][0]) == 9:
            #     break

    # # 使11键, 01键, 10键, 12键, 21键相同
    # if data[1][1] != data[0][1] or data[1][1] != data[1][0] \
    #         or data[1][1] != data[1][2] or data[1][1] != data[2][1]:
    #     while True:
    #         # 按01键
    #         push_01(data, recorder)
    #         # 按10键
    #         push_10(data, recorder)
    #         # 按12键
    #         push_12(data, recorder)
    #         # 按21键
    #         push_21(data, recorder)

    #         if data[1][1] == data[0][1] and data[1][1] == data[1][0] \
    #                 and data[1][1] == data[1][2] and data[1][1] == data[2][1]:
    #             break


def step_one_v2(data, recorder):
    
    if data[0][0] != data[1][1]:
        while True:
            push_00(data, recorder)
            if data[0][0] == data[1][1]:
                break
    if data[0][2] != data[1][1]:
        while True:
            push_02(data, recorder)
            if data[0][2] == data[1][1]:
                break
    if data[2][0] != data[1][1]:
        while True:
            push_20(data, recorder)
            if data[2][0] == data[1][1]:
                break
    if data[2][2] != data[1][1]:
        while True:
            push_22(data, recorder)
            if data[2][2] == data[1][1]:
                break


def step_two_v2(data, recorder):

    if data[0][1] != data[1][1]:
        while True:
            push_00(data, recorder)
            push_02(data, recorder)
            push_21(data, recorder)
            if data[0][1] == data[1][1]:
                break
    if data[1][0] != data[1][1]:
        while True:
            push_00(data, recorder)
            push_20(data, recorder)
            push_12(data, recorder)
            if data[1][0] == data[1][1]:
                break
    if data[2][1] != data[1][1]:
        while True:
            push_01(data, recorder)
            push_20(data, recorder)
            push_22(data, recorder)
            if data[2][1] == data[1][1]:
                break
    if data[1][2] != data[1][1]:
        while True:
            push_02(data, recorder)
            push_10(data, recorder)
            push_22(data, recorder)
            if data[1][2] == data[1][1]:
                break


def diff(a, b):
    """ a的值变成b的值，直接点a所有的方格变成b需要的最小步数 """
    step = b - a
    if a > b:
        step = (b + 9) - a
    return step


def get_value(value, step):
    """ 方格变了step次， 获取该方格的值 """
    value += step
    if value > 9:
        value = value % 9
    return value


if __name__ == '__main__':
    all_in_one()
