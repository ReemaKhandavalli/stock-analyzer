import numpy as np


class MovingAverageStrategy:

    def __init__(self, df):
        self.df = df

    def generate_signals(self):

        self.df["Signal"] = 0

        buy_signal = (
            (self.df["MA_20"] > self.df["MA_50"]) &
            (self.df["MA_20"].shift(1) <= self.df["MA_50"].shift(1))
        )

        sell_signal = (
            (self.df["MA_20"] < self.df["MA_50"]) &
            (self.df["MA_20"].shift(1) >= self.df["MA_50"].shift(1))
        )

        self.df.loc[buy_signal, "Signal"] = 1
        self.df.loc[sell_signal, "Signal"] = -1

        return self.df["Signal"]


    def generate_position(self):

        position = []

        current_position = 0

        for signal in self.df["Signal"]:

            if signal == 1:
                current_position = 1

            elif signal == -1:
                current_position = 0

            position.append(current_position)

        self.df["Position"] = position

        return self.df["Position"]