import csv
import matplotlib.pyplot as plt
import numpy as np
def main():
    file = open('sizee.txt', 'r')
    data = csv.reader(file)
    lst = [row for row in data]
    total_bi = total(lst, 1)
    total_com = total(lst, 2)
    total_net = total(lst, 3)

def total(lst, time):
    count = 0
    for business in lst:
        count += int(business[time])
    print(count)
    return count
