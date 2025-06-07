import random
import time
import threading
from multiprocessing import Queue

class TickerWorker(threading.Thread):
    def __init__(self, input_queue,output_queues, sp500_tickers=['MMM', 'AOS', 'ABT', 'ABBV', 'ACN', 'ADBE', 'AMD', 
                                    'AES', 'AFL', 'A', 'APD', 'ABNB', 'AKAM', 'ALB', 
                                    'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 
                                    'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AEP', 
                                    'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'AME', 'AMGN', 
                                    'APH', 'ADI', 'ANSS', 'AON', 'APA', 'APO', 'AAPL', 'AMAT', 
                                    'APTV', 'ACGL', 'ADM', 'ANET', 'AJG'],
                                    num_tickers=10,**kwargs):
        super(TickerWorker, self).__init__(**kwargs)
        self._tikcers = sp500_tickers[:num_tickers]
        self._output_queues = output_queues
        self.start()


    def run(self):
        """run the worker to extract tickers and put into queue"""
        while True:
            ticker = self._extract_tickers(self._tikcers)
            if ticker is None:
                break
            self._put_tickers_to_queue(ticker, self._output_queues)
            print(f"Ticker {ticker} added to queue.")

    @staticmethod
    def _extract_tickers(tickers):
        """extract the ticker from the list"""
        time.sleep(random.randint(1, 5))
        if tickers:
            return tickers.pop()
    
    @staticmethod
    def _put_tickers_to_queue(tikcer,queue):
        if len(queue) == 1:
            queue[0].put(tikcer)
        else:
            for q in queue:
                q.put(tikcer)



if __name__ == '__main__':
    worker = TickerWorker(Queue())
    worker.run()