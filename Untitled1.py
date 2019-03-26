
# coding: utf-8

# In[118]:


import pandas as pd # добовляем библиотеку pandas 


# In[138]:


mf = pd.read_csv('32432.csv', sep = ',', header = 0) # загружаем данные из файла csv


# In[139]:


result_mf = mf.groupby(['Source','Protocol'])['No.'].count() # осуществляем группировку


# In[135]:


df = pd.DataFrame(result_mf) # преобразовываем в DataFrame

# In[122]:


df = df.rename(columns = {'No.':'Amount'}) # перреименовываем столбец


# In[124]:


df.to_csv('0000.csv') # сохраняем результат в csv файл

