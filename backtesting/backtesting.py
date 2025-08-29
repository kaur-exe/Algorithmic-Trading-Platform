import yfinance as yf
from ..strategies.moving_average import MovingAverageStrategy

class Backtester:
    def __init__(self, symbol="AAPL", start="2020-01-01", end="2021-01-01"):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.strategy = MovingAverageStrategy()

    def run(self):
        data = yf.download(self.symbol, self.start, self.end)
        data = self.strategy.generate_signals(data)

        data['returns'] = data['Close'].pct_change()
        data['strategy_returns'] = data['signal'].shift(1) * data['returns']

        cumulative = (1 + data['strategy_returns']).cumprod()[-1]
        print(f"Final return: {cumulative:.2f}x")

if __name__ == "__main__":
    Backtester().run()