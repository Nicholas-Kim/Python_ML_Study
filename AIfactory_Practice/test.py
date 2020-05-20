import pandas as pd
import numpy as np
import plotly


def read_data(path):
    df = pd.read_csv(path)
    return df


if __name__ == '__main__':
    print('start')
    input_path = './train_input.csv'
    # output_path = './train_output.csv'
    train_input = read_data(input_path)
    # train_output = read_data(output_path)

    save_dict = []

    data = train_input

    for key in data.columns:
        if (key != 'ID') and (key != 'I') and (key != 'J') and (key != 'K'):
           list = data[key].tolist()
           save_dict.append({'key': key, 'avr': np.mean(list), 'variance': np.var(list)})
    print(save_dict)

# for i, data in train_input.iteritems():
#     for (key, value) in data.items():
#         if ((key != 'ID') and (key != 'I') and (key != 'J') and (key != 'K')):
#             sum += data[key]
#             save_dict.append({'key': key, 'sum': sum})

# print(save_dict)
# print('\n')

# save_dict.append({'ID: data['ID'], 'I': data['I'], 'J': data['J'], 'K': data['K'], 'key': key'})

# for i, data in train_input.iterrows():
#     if prev_data is None:
#         prev_data = data
#     else:
#         for (prev_key, prev_value), (key, value) in zip(prev_data.items(), data.items()):
#             if prev_value != value and ((key != 'ID') and (key != 'I') and (key != 'J') and (key != 'K')):
#                 save_dict.append({'ID': data['ID'], 'I': data['I'], 'J': data['J'], 'K': data['K'], 'key': key})
#                 print('save')
#                 print(i)
#         prev_data = data

print('end')
