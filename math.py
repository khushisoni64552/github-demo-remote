#add implimentation
def addition(x,y):
    return x+y

#substract implimentation    
def substract(x,y):
    return x-y       #on master branch

#multiplication implimentation
def multilication(x,y):
    return x*y         #on bug456 branch

#devide implimentation
def devide(x,y):
    if y == 0 :
        return DIVIDE_BY_0_ERROR      #on master branch
    else:
        return x/y

#square implimentation
def square(x):
    return x*x