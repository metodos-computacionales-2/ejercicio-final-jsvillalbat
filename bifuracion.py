#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os
F = np.arange(1.35,1.5,0.0001)


# In[2]:


Theta = []
for Fd in F:
    os.system('./p.x 50000 ' + str(Fd)+ '> data.dat')
    data = np.loadtxt('data.dat')
    Theta.append(data[-1,2])


# In[6]:


import matplotlib.pyplot as plt
plt.scatter(F,Theta)
plt.xlabel('FD')
plt.ylabel('$\Theta$')
plt.grid()
plt.title('Diagrama de Bifuracion')
plt.savefig('bifuracion.png')


# In[ ]:




