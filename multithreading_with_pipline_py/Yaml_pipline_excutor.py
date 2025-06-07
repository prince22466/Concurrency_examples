import importlib
from multiprocessing import Queue
import yaml

class Yaml_pipline_Excute():
    def __init__(self,ymal_file,
                 **kwargs):
        super(Yaml_pipline_Excute, self).__init__(**kwargs)
        self._ymal_file =ymal_file
        self._yaml_data = None
        self._queues={}
        self._workers={}

    def _load_pipline(self):
        with open(self._ymal_file,'r') as yf:
            self._yaml_data = yaml.safe_load(yf)

    def _initiate_queues(self):
        """initiate the queues from the yaml file"""
        for queue in self._yaml_data['queues']:
            queue_name = queue['name']
            self._queues[queue_name] = Queue()

    def _initiate_workers(self):
        """initiate the workers from the yaml file"""
        for worker in self._yaml_data['workers']:
            worker_name = worker['name']
            workerclass = getattr(importlib.import_module(worker['location']),worker['class'])
            input_queue=worker.get('input_queue')
            output_queues = worker.get('output_queue')
            num_instance = worker.get('instance')
            init_params = {
                'input_queue' : self._queues.get(input_queue) if input_queue is not None else None,
                'output_queues':[self._queues.get(q) for q in output_queues] if output_queues is not None else None,
            }

            self._workers[worker_name]=[]
            for i in range(num_instance):
                t = workerclass(**init_params)
                self._workers[worker_name].append(t)
        return


    def _join_workers(self):
        for workers in self._workers:
            for worker_t in self._workers[workers]:
                worker_t.join()

    def process_pipline(self):
        self._load_pipline()
        self._initiate_queues()
        self._initiate_workers()
        self._join_workers()






if __name__ == '__main__':
    Yaml_pipline_Excute_instance=Yaml_pipline_Excute(ymal_file='piplines\wiki_YF_scrapper_pipline.yaml')
    Yaml_pipline_Excute_instance.process_pipline()
    exit()