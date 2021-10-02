from itertools import permutations
import itertools
import os
x=int(input())
r="abcdefghijklmnopqrstuvwxyz0123456789"
l=[]
for i in range(1,x+1):
    l+=[''.join(p) for p in itertools.product(r, repeat=i)]
def create(n):
    file=open('{}.txt'.format(n),'w')
    return file
n=0
file=create(n)
for i in range(len(l)):
    file.write("{}\n".format(l[i]))
    size=os.path.getsize(".\{}.txt".format(n))
    if size>20971520:
        n+=1
        file=create(n)
#s=""
#for i in range(1,n):
 #   s+=permutations(r,n)