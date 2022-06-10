#!/usr/bin/env python
# coding: utf-8

# In[34]:


import os
import dateutil.parser as dp


# In[6]:


class history:
    def __init__(self,epoch_list = [], dict_1 = {}, dict_2 = {}):
        self.epoch_list = epoch_list
        self.dict_1 = dict_1
        self.dict_2 = dict_2
    
    def set_epoch(self,epoch_list):
        self.epoch_list = epoch_list
        return self.epoch_list
    
    def set_history(self,dict_1):
            self.dict_1 = list(dict_1.values())[0]
            return self.dict_1
        
          
def get_epoch_list(history):
    return history.epoch_list
    
def get_accuracy_list(history):
    return history.dict_1
    

def get_accuracy_per_epoch(history):
    a = get_epoch_list(history)
    b = get_accuracy_list(history)
    dict_2 = {}
    for i in a:
        for j in b:
            dict_2[i] = j
            b.remove(j)
            break
    return dict_2
    


# In[ ]:




