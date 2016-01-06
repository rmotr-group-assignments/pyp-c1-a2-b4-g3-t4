def sort_numbers(new_list):
    """sort the list using insertion sort"""

    for num in range(1, len(new_list)):
        hold = new_list[num]
        n = num - 1
        while n >= 0 and new_list[n] > hold:
            new_list[n + 1] = new_list[n]
            n -= 1
        new_list[n + 1] = hold
    return new_list


def get_user_list():
    """get and verify that input is the correct type"""

    user_list = list()
    print('Enter your numbers')
    t = False
    while not t:
        hold = input('> ')

        if hold == '':
            break

        # checks if hold is a number
        try:
            float(hold)
            user_list.append(float(hold))
        except ValueError:
            print('Enter numbers only!')

    return user_list


if __name__ == '__main__':
    new_list = get_user_list()
    print(new_list)
    print(sort_numbers(new_list))
