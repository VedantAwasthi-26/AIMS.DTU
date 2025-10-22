import pandas as pd

lets_say_its_a_csv_file = {
    'Color': ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Cyan', 'White', 'Black']
}
data = pd.DataFrame(lets_say_its_a_csv_file)
print("Original DataFrame:")
print(data)

color_to_int = {
    'Red': 1,
    'Green': 2,
    'Blue': 3,
    'Yellow': 4,
    'Purple': 5,
    'Cyan': 6,
    'White': 7,
    'Black': 0  #don't call me rascist just cz I set black as 0, not saying that I'm not tho :|
}

data['Color_encoded'] = 0

for i in range(len(data)):
    color = data.loc[i, 'Color']
    if color in color_to_int:
        data.loc[i, 'Color_encoded'] = color_to_int[color]
    else:
        data.loc[i, 'Color_encoded'] = 0 
        
data = data.drop(columns=['Color'])

print("\n Ordinal Encoded: ")
print(data)
# LED color coding k ilawa kuch smjh nhi arha tha encoding k liye so i made both the same
#and this was my sasta version of Ordinal Encoding