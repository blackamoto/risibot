import time
import ccxt
import pandas as pd
from jvc import *
from ccxt.base.errors import NetworkError

class StopPostLimit():
    def __init__(self, cookie):
        self.messages = pd.DataFrame(columns=['topic', 'message', 'ticker', 'condition'])
        self.binance = ccxt.binance()
        self.jvc = JVC(cookie)
        self.messages_left = True

    def add_stop_post(self, topic_url: str, message: str, ticker: str, condition: str):
        self.messages = self.messages.append(
            {'topic': topic_url, 'message': message, 'ticker': ticker.upper(), 'condition': condition},
            ignore_index=True)

    def run(self):
        print('Messages en attente: \n')
        print(self.messages[['message', 'ticker', 'condition']], '\n')
        while self.messages_left:
            tickers_to_check = set(self.messages['ticker'].to_list())
            for t in tickers_to_check:
                try:
                    request = self.binance.fetch_trades(symbol=t, limit=1)[0]
                    price = request['price']
                    print(
                        str(pd.to_datetime(request['timestamp'], unit='ms')) + ' ' + t + ' = ' + str(price))
                except NetworkError:
                    pass
                else:
                    for index, row in self.messages.loc[self.messages['ticker'] == t].iterrows():
                        if eval(str(price) + row['condition']):
                            self.jvc.postTopic(url=row['topic'], message=row['message'])
                            self.messages=self.messages.drop([index])
                            print("message posté")
                            print(self.messages)
                            if self.messages.shape[0] == 0:
                                self.messages_left = False

                time.sleep(0.3)
            time.sleep(5)


c=""
client=StopPostLimit(c)