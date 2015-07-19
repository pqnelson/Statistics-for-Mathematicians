import matplotlib as mpl

mpl.use("pgf")
pgf_with_pdflatex = {
    "pgf.texsystem": "pdflatex"
}
mpl.rcParams.update(pgf_with_pdflatex)
import numpy as np
import matplotlib.pyplot as plt
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=10)
import math

# Stirling's approximation
def factorial(n):
    x = 1.0*n
    return math.sqrt(2*math.pi*x)*math.pow(x/math.e,x)

# return a*(a+1)*(...)*b
def product(a, b):
    if a>b:
        return product(b,a)
    else:
        result = 1.0
        for k in xrange(a,b+1):
            result = result*k
        return result

# probability X = D
def hypergeometricProbability(X):
    c = 990.0
    return c*(X*(X-1)*0.5) * product(902-X+1,900)/product(1000-X+1,1000)

def moosePopulation(N):
    c = 1192725059258223539848800000.0
    return c * product(N-200,N-241)/product(N-49,N)

#for N in xrange(1242, 1261):
#    v = moosePopulation(N)
#    print "N=%d, h(N,50,200,8) = %.20f" % (N,v)

x = range(200,5000,50)
y = [moosePopulation(point) for point in x]
phi = 0.5*(1 + math.sqrt(5))
width = 4.5
plt.figure(figsize=(width, width/phi))
plt.plot(x, y, 'b',[1247],[moosePopulation(1247)],'ro')
plt.title('Moose Population',fontsize=10)
plt.show()
plt.savefig('moose.pdf', bbox_inches='tight')
