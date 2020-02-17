#!/usr/bin/env python3

from Employee import Employee
import pickle

ObjEmployee = Employee('Mary', 88803223545, 50000)
with open('pickle.test', 'wb') as F:
    pickle.dump(ObjEmployee, F)
