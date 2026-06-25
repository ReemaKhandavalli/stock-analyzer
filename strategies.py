import numpy as np


class MovingAverageStrategy:
    def __init__(self, df):
        self.df = df

    def generate_position(self):
        self.df["Position"] = np.where(
            self.df["MA_20"] > self.df["MA_50"],
            1,
            0
        )

        return self.df["Position"]