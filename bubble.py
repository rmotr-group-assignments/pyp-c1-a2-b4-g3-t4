"""Bubble sort algorithm"""


def bubble(unsorted_list):
    """sorts the list"""

    new_list = unsorted_list
    s = False
    while not s:
        s = True
        for i in range(len(unsorted_list) - 1):
            if new_list[i] > new_list[i+1]:
                s = False
                new_list[i], new_list[i+1] = new_list[i+1], new_list[i]
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


unsorted = get_user_list()
print(unsorted)
print(bubble(unsorted))
