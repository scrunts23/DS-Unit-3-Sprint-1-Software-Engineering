import pandas as pd
import sklearn
import sklearn.model_selection
from sklearn.model_selection import train_test_split
from scipy.stats import ttest_ind

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

def train_split(df):
    '''
    A split function that splits a dataframe into a 70/30 train test split
    '''
    train, test = train_test_split(df, train_size=.70, random_state=42)
    return train, test