import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt
from matplotlib import style

# style.use('ggplot')
# x=[1,3,5,7,9,11,13]
# x2=[2,4,6,8,10,12,14]
# y=[50,51,52,48,47,49,46]
# y2=[50,23,45,76,54,65,66]
# plt.xlabel('Day')
# plt.ylabel('Temperature')
# plt.title('Weather')

# ## { for plot graph
# plt.plot(x,y,color='green',label='line one',linewidth=2)
# plt.plot(x,y2,color='blue',label='line one',linewidth=2)
# # ## }
# # ## { for bar graph 
# # plt.bar(x,y,color='green',label='line one',linewidth=2)
# # plt.bar(x2,y2,color='blue',label='line one',linewidth=2)
# # ## }


# plt.legend()
# plt.grid(True,color='k')

# plt.show()


# ## { 

# for histogram
# x=[61,3,23,13,28,32,32,35,35,24,23,55,34,46,53,43,32,11,66,89,96,90,45,78]
# bins=[0,10,20,30,40,50,60,70,80,90,100]

# plt.hist(x,bins,rwidth=0.9,histtype='bar')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Histogram')
# plt.legend()
# plt.show()

# ## }


# ## { for scatter Plot

# x=[1,2,3,4,5,6,7,8]
# y=[3,4,7,6,8,9,5,4]
# y1=[3,5,6,7,8,5,5,6]

# plt.scatter(x,y,label='skitscat',color='red')
# plt.scatter(x,y1,label='skitscat',color='blue')
# ## plt.plot(x,y,color='green',label='line one',linewidth=2)
# ## plt.plot(x,y1,color='yellow',label='line one',linewidth=2)


# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Scatter Plot')
# plt.legend()
# plt.show()
    
# ## }

# ## { for Stck Plot


# days =[1,2,3,4,5]
# sleeping=[7,8,6,11,7]
# eating = [2,3,4,3,2]
# working = [7,8,7,2,2]
# playing = [8,5,7,8,13]
# # days =[1,2,3,4,5]
# # sleeping=[1,2,3,4,5]
# # eating = [1,2,5,4,5]
# # working = [5,4,3,2,1]
# # playing = [5,4,3,2,1]

# plt.plot([],[],color='m',label='Sleeping',linewidth=5)
# plt.plot([],[],color='c',label='Eating',linewidth=5)
# plt.plot([],[],color='r',label='Working',linewidth=5)
# plt.plot([],[],color='k',label='Playing',linewidth=5)

# plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Stck Plot')
# plt.legend()
# plt.show()


# ## }


# ## {

# x=[7,2,2,13]
# y=['Sleeping','eating','working','playing']
# cols=['c','m','r','b']

# plt.pie(x,
#     labels=y,
#     colors=cols,
#     startangle=90,
#     shadow=True,
#     explode=(0,0.1,0,0),
#     autopct='%1.1f%%'
# )
# plt.title('Pie Plot')
# # plt.legend()
# plt.show()

# ## }

## {

import numpy as np
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0.0,5.0,0.1)
t2 = np.arange(0.0,5.0,0.02)

plt.subplot(221)
plt.plot(t1,f(t1),'bo',t2,f(t2))

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2))
plt.show()



## }

