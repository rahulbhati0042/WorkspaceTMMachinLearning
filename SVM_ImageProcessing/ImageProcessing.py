import sklearn.datasets
import sklearn.svm
import matplotlib.pyplot
import numpy

# x = features and y = targets
x,y = sklearn.datasets.make_blobs(n_samples=100,centers=2,n_features=2,random_state=20)

Classified= sklearn.svm.SVC(kernel='linear',C=500)
print(type(Classified))

Classified.fit(x,y)
#print('[x[1][0],x[1][1]]',[x[1][0],x[1][1]])

queryData1 = [[5,6]]
queryData2 = [[2.5,6.4]]
print('actual target y[0]= ',y[0])
print('actual target y[1]= ',y[1])

results_query1= Classified.predict(queryData1)
results_query2= Classified.predict(queryData2)
print('predicted queryData1= ',results_query1)
print('predicted queryData2= ',results_query2)

#print(x)
#print("Zero vala Colunm : ",x[:,0])
#print("*"*50)
#print("One vala Colunm Data : ",x[:,1])

###### Plot both 2 featrues
# asssign colormap
colormap = numpy.array([('red'), ('blue')])
matplotlib.pyplot.scatter(x[:,0],x[:,1],c=colormap[y])

##### Plot query points
matplotlib.pyplot.scatter(queryData1[0][0],queryData1[0][1],c='red',s =100,edgecolors='k')
matplotlib.pyplot.scatter(queryData2[0][0],queryData2[0][1],c='yellow',s =100,edgecolors='red')

### GCA Function###
#matplotlib.pyplot.gca() Function:  gca = get current axes
#The gca() function in pyplot module of matplotlib library is used to get the current Axes instance on the current figure matching the given keyword args, or create one.
#Or this function give us the scaling of x and y. means scaling btata he of x and y kaa.

axes = matplotlib.pyplot.gca()
print(axes)

#print('axes x limit and y limit')
xlim=axes.get_xlim()
ylim= axes.get_ylim()
print('xlim=',xlim,'ylim=',ylim)

print("########### Randome Arrays############")
xx =numpy.random.uniform(xlim[0],xlim[1],size=5)
yy =numpy.random.uniform(ylim[0],ylim[1],size=5)
print(type(xx),'xx shape=',xx.shape)
print('xx',xx)
print('yy',yy)
print(type(yy),'yy shape=',yy.shape)

print("############ Creating Meshgrid##########")
xxx,yyy = numpy.meshgrid(xx,yy)
print('xxx=',xxx)
print('yyy=',yyy)
print()

print("########### Flatton ############")
print(type(xxx),xxx.shape)
xxx_flatton = xxx.ravel()
yyy_flatton = yyy.ravel()
print('xxx_flatton=',xxx_flatton)
print('yyy_flatton=',yyy_flatton)
print()

print("########### Concatenate two array ############")
xxxyyy = numpy.c_[xxx_flatton,yyy_flatton]
print(type(xxxyyy),xxxyyy.shape)
print(xxxyyy)

print("########### Decision Function ############")
print()
zz = Classified.decision_function(xxxyyy)
print(zz,type(zz),zz.shape)
zz_u = zz.reshape(5,5)
print('zz_u',type(zz_u),zz_u.shape)
 
print("########### Contour plots ############")
matplotlib.pyplot.contour(xx,yy,zz_u, levels=[-1,0,1],
                          linestyles= ['solid','dashed','solid'],
                          colors = ('red','green','blue'),
                          linewidths=3
)
print("########### Following are the support vectors ############")
support_vecotrs = Classified.support_vectors_
print(support_vecotrs)
matplotlib.pyplot.scatter(support_vecotrs[:,0],support_vecotrs[:,1],c='black',
                          facecolor=None,s =200,edgecolors='g',
                          linewidths=2)

matplotlib.pyplot.show()