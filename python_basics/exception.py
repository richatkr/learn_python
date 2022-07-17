# Exception handelling in python
x=input('Enter Integer1 : ')
y=input('Enter Integer2 : ')
try:
    z=int(x)/int(y)
# For handelling divided by 0 exception 
# to get the name of occured exception type(e).__name__
except ZeroDivisionError as e:
    print('Exception occured : ',type(e).__name__)
    z = None
# if user forgot to change input value into interger 
except TypeError as e:
    print('Exception occured : ',type(e).__name__)
    z=None
# if user not know the name of Exception use 
# except Exception as e 
# then to get the name of defined Exception type(e).__name__

print('Division is : ',z)