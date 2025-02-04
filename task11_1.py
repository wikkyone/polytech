from sklearn.model_selection import train_test_split
import pandas as pd


def split_data(file_name, Y):
    data = pd.read_csv(file_name, index_col=0)
    features = data.drop(Y, axis=1)
    target = data[Y]
    features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.25, random_state=42)
    return [features_train, features_test, target_train, target_test]
