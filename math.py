#Add implimentation
def addition(x,y):
    return x+y

#Substract implimentation    
def substract(x,y):
    return x-y       #on master branch

#Multiplication implimentation
def multilication(x,y):
    return x*y         #on bug456 branch

#Devide implimentation
def devide(x,y):
    if y == 0 :
        return DIVIDE_BY_0_ERROR      #on master branch
    else:
        return x/y

#Square implimentation
def square(x):
    return x*x