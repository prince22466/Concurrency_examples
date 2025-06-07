import threading
import random
import queue as pyqueue
import time
import logging # For better diagnostics

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class RandomPriceWorkers(threading.Thread):
    def __init__(self,input_queue,output_queues,
                 **kwargs):
        super(RandomPriceWorkers, self).__init__(**kwargs)
        self._queue =input_queue#symbol queue
        self._outqueues=output_queues#price queue
        self.start()

    @staticmethod
    def take_symbol(queue):
        """take the symbol from the queue"""
        while True:
            try:
                print("RandomPriceWorker try get symbol from symbol queue. the symbol queue is ",
                      "empty" if queue.empty() else "Not empty.")
                # Attempt to get a symbol from the queue with a timeout
                symbol = queue.get(timeout=10)
                print("RandomPriceWorker get symbol from symbol queue, which is ", symbol)
            except pyqueue.Empty:
                logger.warning("symbol Queue is empty for 10 sec, no symbol retrieved.")
                break
            if symbol == "The End":
                print("RandomPriceWorker get The End from symbol queue, return None")
                return None
            return symbol

    @staticmethod
    def ticker_price_generator(ticker):

        if ticker is None:
            return (None, None)
        rand_sleep_sec= random.randint(0,10)
        time.sleep(rand_sleep_sec)  # Sleep for 10 second to avoid overwhelming the server

        price =random.randint(0,10**6)
        return (ticker,float(price))

    @staticmethod
    def price_to_queue(price_info, output_queues):
        if output_queues is not None:
            for out_queue in output_queues:
                out_queue.put(price_info)


    def run(self):
        while True:
            ticker = self.take_symbol(self._queue)
            if ticker is None:
                break
            priceinfo = self.ticker_price_generator(ticker)
            self.price_to_queue(priceinfo,self._outqueues)

if __name__ == '__main__':
    price_None = RandomPriceWorkers.ticker_price_generator(None)
    print(price_None)
    price_ticker = RandomPriceWorkers.ticker_price_generator('APPL')
    print(price_ticker)
