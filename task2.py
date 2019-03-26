
# coding: utf-8

# In[117]:


import pandas as pd #добовляем библиотеку


# In[118]:


df = pd.read_csv('original.csv', header=0 , sep = ',')#открываем файл csv


# In[119]:


df.drop(df.columns[[0,1]],axis = 'columns',inplace = True)#удаляем столбцы


# In[120]:


tcp = pd.DataFrame(df[df['Protocol']=="TCP"])#выбираем интересующие строки с TCP протоколом


# In[121]:


tcp = pd.DataFrame(tcp.groupby(['Source','Destination','Dist_port','Source_port'])['Source'].count())#группируем для подсчета количества обращения по ip адресам


# In[122]:


tcp = result.rename(columns={'Source':'Amount'})#переименовываем столбец подсчета


# In[123]:


tcp.sort_values(by = ['Amount'], ascending = False , inplace = True)#сортируем по убыванию


# In[124]:


tcp.to_csv('result.csv')#сохраняем в csv формат

