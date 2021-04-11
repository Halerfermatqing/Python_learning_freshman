import pandas as pd
import numpy as np

# a = pd.Series([1, 2, 2])
# print(a)
# print(type(a))
# t3 = {"name": "xiaomin", "age": 90, "tel": 10086}
# t3 = pd.Series(t3)
# print(t3)
# t3.astype("object")
# print(t3.index)
# print(type(t3.index))
# print(list(t3.index))
# print(t3.values)
# print(type(t3.values))
# print(list(t3.values))

t2 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(t2)

t2 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list("qwe"), columns=list("asdf"))
print(t2)
print("*" * 10)
print(t2.info())
# help(pd.Series)
