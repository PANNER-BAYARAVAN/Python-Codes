import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8,4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

print (df.loc[:,['A','C']])
