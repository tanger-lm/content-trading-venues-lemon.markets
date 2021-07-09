import os
from dotenv import load_dotenv
from helpers import RequestHandler


class TradingVenueInstrument(RequestHandler):
    def get_trading_venue_instruments(self):
        load_dotenv()
        mic = os.getenv("MIC")
        endpoint = f'trading-venues/{mic}/instruments/?search=Tesla&type=stock'
        response = self.get_data(endpoint)
        print(response)


if __name__ == "__main__":
    TradingVenueInstrument().get_trading_venue_instruments()