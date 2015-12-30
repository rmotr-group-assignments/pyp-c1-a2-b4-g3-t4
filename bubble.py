"""Bubble sort algorithm"""

def bubble(unsorted):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(unsorted) -1):
            if unsorted[i] > unsorted[i+1]:
                sorted = False
                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]

