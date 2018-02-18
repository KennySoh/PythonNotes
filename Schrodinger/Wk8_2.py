# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 19:31:41 2017

@author: yang
"""


from mayavi import mlab
for i in range(n):#l=0,1,2,3
        for j in range(-i,i+1):
            xdata = "xdata{}{}{}.dat".format(n,i,j)
            ydata = "ydata{}{}{}.dat".format(n,i,j)
            zdata = "zdata{}{}{}.dat".format(n,i,j)
            magdata = "density{}{}{}.dat".format(n,i,j)

            x=np.load(xdata)
            y=np.load(ydata)
            z=np.load(zdata)
            density=np.load(magdata)
            
            figure = mlab.figure('DensityPlot{}{}{}'.format(n,i,j))
            mag=density/np.amax(density)
            #pts = mlab.points3d(mag ,opacity =0.5, transparent=True)
            pts = mlab.contour3d(mag, opacity=0.5)
            mlab.colorbar(orientation='vertical')
            mlab.axes ()
            mlab.savefig("{}{}{}_mayavi.png".format(n,i,j))
            print "{}{}{}.png saved".format(n,i,j)
print "Completed"