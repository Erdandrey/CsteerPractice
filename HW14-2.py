#!/usr/bin/env python3

import pickle
with open('pickle.test', 'rb') as F:
    NewEmployee = pickle.load(F)
NewEmployee.print_salary_info()

