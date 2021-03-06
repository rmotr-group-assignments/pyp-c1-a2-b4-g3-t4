"""Bubble sort algorithm"""


def bubble(user_list):
    """sorts the list"""

    s = False
    while not s:
        s = True
        for i in range(len(user_list) - 1):
            if user_list[i] > user_list[i+1]:
                s = False
                user_list[i], user_list[i+1] = user_list[i+1], user_list[i]
    return user_list


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
    unsorted = get_user_list()
    print(unsorted)
    print(bubble(unsorted))
