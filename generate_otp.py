#!/usr/bin/env python
# coding: utf-8

# In[31]:


import random
import smtplib


# In[26]:


otp = ''
for i in range(6):
    otp = otp + str(random.randint(0,9))


# In[30]:


otp

