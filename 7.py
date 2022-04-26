import pandas as pd
d = "строка подстрока"
print(pd.Series(list(d)).value_counts())