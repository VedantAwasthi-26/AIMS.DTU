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
    mean = imp_data[col].mean(skipna=True)
    imp_data[col].fillna(mean, inplace=True)

print("\n after Mean Imputation:")
#only did mean imputation cz the requirements were never to make a "good" code
print(imp_data)

#and this was my sasta version of SimpleImputer