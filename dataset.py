import constants
import pandas as pd


class Dataset:
    """
    Singleton dataset wrapper
    """

    def __init__(self):
        self.df = pd.read_csv(constants.DATASET_FNAME)
        self._X = self.df.drop(columns=['is_safe'])
        self._y = self.df['is_safe']
        self._X -= self._X.mean()
        self._X /= self._X.std()

    @property
    def X(self):
        return self._X

    @property
    def y(self):
        return self._y