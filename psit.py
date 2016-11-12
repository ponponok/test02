import csv
import matplotlib.pyplot as plt
import numpy as np
def main():
    file = open('sizee.txt', 'r')
    data = csv.reader(file)
    lst = [row for row in data]
