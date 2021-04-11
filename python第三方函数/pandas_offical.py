import numpy as np
import pandas as pd
s = pd.Series(np.random.randn(5),index=['a','b','c','d','e',])
print(s)

print(s.index)

print('*'*10)

print(pd.Series(np.random.randn(5)))

d = {'b':'jash','j':'jack'}
print(pd.Series(d))

print(pd.Series(5,index=['a','b','c','d']))

print(pd.Series(np.random.rand(6)).to_numpy())