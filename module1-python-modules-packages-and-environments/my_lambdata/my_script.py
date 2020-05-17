import pandas as pd
import numpy as np


def start():
    options = {
        'display': {
            'max_columns': None,
            'max_colwidth': 25,
            'expand_frame_repr': False,  # Don't wrap to multiple pages
            'max_rows': 14,
            'max_seq_items': 50,         # Max length of printed sequence
            'precision': 4,
            'show_dimensions': False
        },
        'mode': {
            'chained_assignment': None   # Controls SettingWithCopyWarning
        }
    }

    for category, option in options.items():
        for op, value in option.items():
            pd.set_option(f'{category}.{op}', value)  # Python 3.6+

if __name__ == '__main__':
    start()
    del start


def split_train_val_test(df,val_ratio,test_ratio):
    shuffled_indcies=np.random.permutation(len(df))
    val_set_size= int(len(df)*val_ratio)
    val_indcies=shuffled_indcies[:val_set_size]
    test_set_size= int(len(df)*test_ratio)
    test_indcies=shuffled_indcies[val_set_size:test_set_size+val_set_size]
    train_indices=shuffled_indcies[test_set_size:]
    return df.iloc[train_indices],df.iloc[val_indcies],df.iloc[test_indcies]