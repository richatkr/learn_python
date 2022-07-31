from unicodedata import name
import pandas as pd
import numpy as np
def gradient_descent(x,y):
    m_curr = b_curr = 0
    x_diff = 0
    y_diff = 0
    learning_rate = 0.0001 
    iteration = 1000
    x= np.array([1,2,3,4,5])
    y= np.array([5,7,9,11,13])
    n=len(x) 
    for i in range(iteration):
        y_predict = m_curr * x  + b_curr
        m_derivative = -(2/n)*sum(x*(y+y_predict))
        b_derivative = -(2/n)*sum(y+y_predict)

        m_curr = m_curr - learning_rate * m_derivative
        b_curr = b_curr - learning_rate * b_derivative

        print('m{}, b{}, iteration{} '.format(m_curr,b_curr,i))
        
if(__name__ == "__main__"):
    gradient_descent(0,0)