import yfinance as yf


class StockDataLoader:

    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker.upper()
        self.start_date = start_date
        self.end_date = end_date

    def load_data(self):

        df = yf.download(
            self.ticker,
            start=self.start_date,
            end=self.end_date,
            progress=False
        )

        df.reset_index(inplace=True)

        return df