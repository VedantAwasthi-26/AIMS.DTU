import pandas as pd
import numpy as np

lets_say_its_a_csv_file = {
    'Something': [52, np.nan, 30, 22, np.nan],
    'Something_else': [80, 90, np.nan, 70, 85]
}

data = pd.DataFrame(lets_say_its_a_csv_file)
print("Original :")
print(data)

imp_data = data.copy()

for col in imp_data.columns:
    mean = imp_data[col].mean()
    mode =imp_data[col].mode()[0]
    val = (mean + mode)/2
    imp_data[col].fillna(val, inplace=True)

print("\n after Mean Imputation:")
print(imp_data)
