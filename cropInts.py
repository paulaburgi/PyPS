#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:22:32 2019

@author: pmb229
"""

import numpy as np
import isceobj
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap
import cv2
import os

os.chdir('/data/pmb229/isce/p222f870/Sentinel_p13f446/ints')
params = np.load('params.npy',allow_pickle=True).item()
locals().update(params)
geom = np.load('geom.npy',allow_pickle=True).item()
locals().update(geom)


# crop area
y1 = 980
y2 = 2316
x1 = 1988 
x2 = 2892
nxl2 = x2-x1
nyl2 = y2-y1


# crop geom
lo = geom['lon_ifg'][y1:y2,x1:x2]
la = geom['lat_ifg'][y1:y2,x1:x2]
hgt = geom['hgt_ifg'][y1:y2,x1:x2]
print(lo.shape)

geom = {}
geom['lon_ifg'] = lo
geom['lat_ifg'] = la
geom['hgt_ifg'] = hgt
np.save('geom_2.npy',geom)

params['nxl'] =          nxl2
params['nyl'] =          nyl2
params['ymin'] =         0
params['ymax'] =         nyl2
np.save('params_2.npy',params)

 # crop ints
for pair in params['pairs']:
    infile = params['intdir']+ '/' + pair+'/fine_lk.r4'
    outfile = params['intdir']+ '/' + pair+'/fine_lk_crop.r4'
    i  = isceobj.createImage() 
    i.load(infile + '.xml')
    i1 = i.memMap()[:,:,0]
    i2 = i1[y1:y2,x1:x2]
    
    # Write out the xml file for the cropped ifg
    out = i.clone() # Copy the interferogram image from before
    out.filename = outfile
    out.width = nxl2
    out.length = nyl2
    out.dump(outfile + '.xml') # Write out xml
    i2.tofile(outfile)
    out.renderHdr()
    out.renderVRT() 
    
# crop cor files
for pair in params['pairs']:
    infile = params['intdir']+ '/' + pair+'/cor_lk.r4'
    outfile = params['intdir']+ '/' + pair+'/cor_lk_crop.r4'
    i  = isceobj.createImage() 
    i.load(infile + '.xml')
    i1 = i.memMap()[:,:,0]
    i2 = i1[y1:y2,x1:x2]
    
    # Write out the xml file for the cropped ifg
    out = i.clone() # Copy the interferogram image from before
    out.filename = outfile
    out.width = nxl2
    out.length = nyl2
    out.dump(outfile + '.xml') # Write out xml
    i2.tofile(outfile)
    out.renderHdr()
    out.renderVRT() 
        
        
        
        
        
# crop big time series
infile = 'TS/rates_flat.unw'
outfile = 'TS/rates_flat_2.unw'
i  = isceobj.createImage() 
i.load(infile + '.xml')
i1 = i.memMap()[:,:,0]
i2 = i1[y1:y2,x1:x2]

# Write out the xml file for the cropped ifg
out = i.clone() # Copy the interferogram image from before
out.filename = outfile
out.width = nxl2
out.length = nyl2
out.dump(outfile + '.xml') # Write out xml
i2.tofile(outfile)
out.renderHdr()
out.renderVRT()         
        
        
        
        
        
        
        
        
        
        
        
        