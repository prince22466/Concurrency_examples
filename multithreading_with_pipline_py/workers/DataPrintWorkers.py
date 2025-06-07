import threading
import logging # For better diagnostics
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DataPrintWorkers(threading.Thread):
    def __init__(self,input_queue,output_queues,
                 **kwargs):
        super(DataPrintWorkers, self).__init__(**kwargs)
        self._queue =input_queue#price queue
        self._outputs = output_queues
        self.start()

    @staticmethod
    def take_price(queue):
        """take the price from the data_print_queue queue"""
        try:
            print("DataPrintWorker try get info from dataprint queue. the dataprint queue is ",
                    "empty" if queue.empty() else "Not empty.")
            priceinfo = queue.get(timeout=10)
            print("DataPrintWorker get info from symbol queue, which is ", priceinfo)
        except:
            logger.warning("dataprint Queue is empty for 10 sec, no priceinfo retrieved.")
            return (None,None)
        return priceinfo

 
    def run(self):
        while True:
            price = self.take_price(self._queue)
            print(price)
            if price ==(None,None):
                break


if __name__ == '__main__':
    pass