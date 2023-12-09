#!/usr/bin/env python3

import os
from time import perf_counter_ns

def get_differences(values):
    return [values[ix+1] - values[ix] for ix in range(len(values) - 1)]

def get_next_value(line):
    values = [int(value) for value in line.split(' ') if value != '']
    difference_list = []
    differences = get_differences(values)
    while not all(map(lambda x: x == 0, differences)):
        difference_list.append(differences)
        differences = get_differences(differences)
    return values[-1] + sum([differences[-1] for differences in difference_list])

def answer(input_file):
    start = perf_counter_ns()
    with open(input_file, 'r') as input:
        data = input.read().split('\n')

    answer = sum([get_next_value(line) for line in data])
    end = perf_counter_ns()

    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), 'input')
answer(input_file)
