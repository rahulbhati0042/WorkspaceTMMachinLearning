import sklearn.datasets
import sklearn.svm
import numpy
import matplotlib.pyplot

x,y = sklearn.datasets.make_blobs(n_samples=100,n_features=2,centers=2,random_state=20)
Classified = sklearn.svm.SVC(kernel='linear', C=500)
Classified.fit(x,y)
# asssign colormap
colormap = numpy.array([('red'), ('blue')])
matplotlib.pyplot.scatter(x[:,0],x[:,1],c=colormap[y])

axes = matplotlib.pyplot.gca()
xlim = axes.get_xlim()
ylim = axes.get_ylim()

xx = numpy.random.uniform(xlim[0],ylim[1], size=5)
yy = numpy.random.uniform(ylim[0],ylim[1],size=5)

xxx, yyy = numpy.meshgrid(xx,yy)

xxx_flatton = numpy.ravel(xxx)
yyy_flatton = numpy.ravel(yyy)

xxx_yyy = numpy.c_[xxx_flatton,yyy_flatton]

zz = Classified.decision_function(xxx_yyy)
zz_u = zz.reshape(5,5)
matplotlib.pyplot.contour(xx,yy,zz_u,levels=[-1,0,1],linestyles=['solid','dashed','solid'],colors=['green','blue','yellow'],
                        linewidths=3)

support_vectors = Classified.support_vectors_
print(support_vectors)
matplotlib.pyplot.scatter(support_vectors[:,0],support_vectors[:,1],c='black',
                          facecolor=None,s =200,edgecolors='g',
                          linewidths=2)
matplotlib.pyplot.show()