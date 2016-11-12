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
    avcom, avnet = average(lst, total_com, total_net)

def average(lst, total_com, total_net):
    averg = []
    for com in lst:
        averg.append([(int(com[2])/total_com*100), (int(com[3])/total_net*100)])
    avcom = [com for com, net in averg]
    avnet = [net for com, net in averg]
    return avcom, avnet
