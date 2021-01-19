# coding=<utf-8>

"""
(ref) https://youtu.be/58fuWVu5DVU?t=336
"""


#%%
import numpy as np 
import matplotlib.pyplot as plt



# %% 입력 벡터 생성; 2-tuple
np.random.seed(42)



x1 = np.random.randn(10) * 100
x2 = np.random.randn(10) * 10


plt.axvline(x=0, color='gray')
plt.axhline(y=0, color='gray')
plt.scatter(x1, x2, color='black')
plt.show()



# %% 표준화된 입력 벡터 
"""
입력 벡터가 zero-centered 된다.

"""


norm_x1 = (x1 - np.mean(x1)) / np.std(x1)
norm_x2 = (x2 - np.mean(x2)) / np.std(x2)


plt.axvline(x=0, color='gray')
plt.axhline(y=0, color='gray')
plt.scatter(norm_x1, norm_x2, color='black')
plt.show()
# %%