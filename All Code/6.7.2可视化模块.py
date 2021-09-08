import matplotlib.pyplot as plt
import numpy as np
def normal():
    n = 1024
    x = np.random.normal(0,1,n)
    y = np.random.normal(0,1,n)
    plt.scatter(x,y)
    plt.show()
def sincos():
    x = np.linspace(-np.pi,np.pi,256,endpoint=True)
    c,s = np.cos(x),np.sin(x)
    plt.plot(x,c)
    plt.plot(x,s)
    plt.show()

def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

def samehighgraph():
    n = 256
    x = np.linspace(-3,3,n)
    y = np.linspace(-3,3,n)
    X,Y = np.meshgrid(x,y)
    plt.contourf(X,Y,f(X,Y),8,alpha = .75,cmap = 'jet')
    C = plt.contour(X,Y,f(X,Y),8,colors = 'black',lineweight = .5)
    plt.show()

if __name__ == "__main__":
    # sincos()
    samehighgraph()