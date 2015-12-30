"""Bubble sort algorithm"""


def bubble(unsorted):
    sorted = False
    l = len(unsorted) - 1
    while not sorted:
        sorted = True
        for i in range(l):
            if unsorted[i] > unsorted[i+1]:
                sorted = False
                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
    return unsorted


def get_user_list():
    user_list = list()
    print('Enter your numbers: ')
    t = False
    while not t:
        hold = input('> ')
        if hold == '':
            break
        try:
            float(hold)
            user_list.append(float(hold))
        except ValueError:
            t = False
            print('Enter numbers only!')

    return user_list


unsorted = get_user_list()
print(unsorted)
print(bubble(unsorted))
