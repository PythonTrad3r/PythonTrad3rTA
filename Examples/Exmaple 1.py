import PythonTrad3rTA as TA
import yfinance as yf
from datetime import date

# Yahoo Finance API parameters. 
ticker = "AAPL"
start = date(2019, 1, 1)
end = date.today()

# Historical data of the ticker.
hist = yf.download(ticker, start, end)

# Sends only the close and gets back the current RSI value.
RSI = TA.Indicators.RSI(hist['Close'])

# Sends only the close and EMA span. Returns the current 200 EMA value.
EMA_200 = TA.Indicators.EMA(hist['Close'], 200)

# Sends historical data and gets back both stochastic K and stochastic D.
stoch_K, stoch_D = TA.Indicators.stochastic(hist)

# Gets the most current candle.
currentCandle = hist.iloc[0]

# Sends the most current candle and gets back if it is bearish/bullish pin or returns 0 if not.
isPinbar = TA.CandlePatterns.PinBar(currentCandle)

# Sends the most current candle and gets back if it is bearish/bullish engulfing or returns 0 if not.
isEngulfing = TA.CandlePatterns.Engulfing(hist)

# Sends the most current candle and gets back if it is golden/death cross or returns 0 if not.
golden_death_cross = TA.ChartPatterns.EMAGoldenDeathCross(hist)
