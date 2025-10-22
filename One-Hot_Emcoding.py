import pandas as pd

lets_say_its_a_csv_file = {
    'Color': ['Purple', 'Blue', 'Cyan', 'Yellow', 'Red', 'Green', 'White', 'Black']
}
data = pd.DataFrame(lets_say_its_a_csv_file)
print("Original DataFrame:")
print(data)

color_to_rgb = {
    'Red':    [1, 0, 0],
    'Green':  [0, 1, 0],
    'Blue':   [0, 0, 1],
    'Yellow': [1, 1, 0],
    'Purple': [1, 0, 1],
    'Cyan':   [0, 1, 1],
    'White':  [1, 1, 1],
    'Black':  [0, 0, 0]
}

data['R'] = 0
data['G'] = 0
data['B'] = 0

for i in range(len(data)):
    color = data.loc[i, 'Color']
    if color in color_to_rgb:
        data.loc[i, ['R', 'G', 'B']] = color_to_rgb[color]

data = data.drop(columns=['Color'])

print("\nRGB Encoded DataFrame:")
print(data)
# LED color coding k ilawa kuch smjh nhi arha tha encoding k liye so i made both the same
#and this was my version of One-Hot Encoding