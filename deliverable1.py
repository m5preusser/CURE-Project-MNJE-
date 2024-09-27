# task1.py 
# ENDG 319
# CURE Project
# September 20, 2024
# Contributers:
#   Matthias Preusser (30206565)
#   JP Hoffman ()
#   Noah Crawford ()
#   Evan Myers ()

# Imports
import pandas as pd
from sklearn.datasets import load_digits, load_breast_cancer

def task1():
    efficiency = {
        "Gasoline (MPG)": []
    }

def task2():
    pass

def task3():
    pass

def task4():
    digits_dataset = load_digits()
    print(digits_dataset.keys())
    print(digits_dataset.DESCR)
    
    breast_cancer = load_breast_cancer()
    print(breast_cancer.keys())
    print(breast_cancer.DESCR)

