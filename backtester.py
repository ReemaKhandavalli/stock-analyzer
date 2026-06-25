class Backtester:
    def __init__(self, df):
        self.df = df

    def strategy_returns(self):
        self.df["Strategy Return"] = (
            self.df["Daily Return"] * self.df["Position"]
        )

        return self.df["Strategy Return"]

    def buy_and_hold_returns(self):
        return self.df["Daily Return"]

    def strategy_equity_curve(self):
        return (1 + self.df["Strategy Return"]).cumprod()

    def buy_and_hold_equity_curve(self):
        return (1 + self.df["Daily Return"]).cumprod()