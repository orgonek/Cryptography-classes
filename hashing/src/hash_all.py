import hashlib
import timeit

class HashAll:
    """ Class used for perform text and file hashing """
    def __init__(self):
        pass

    def perform_hashing(self, text : str) -> dict:
        """ Performs hashing using available functions and calculates the execution time for each algorithm """
        
        results = {}

        for algorithm in sorted(hashlib.algorithms_available):
            obj = hashlib.new(algorithm)
            
            start = timeit.default_timer()

            obj.update(text.encode('utf-8'))

            results[algorithm] = {}
            
            results[algorithm]['hexdigest'] = obj.hexdigest(64) if 'shake' in algorithm else obj.hexdigest()
            
            stop = timeit.default_timer()

            results[algorithm]['time'] = (stop - start)
            

        return results

    def perform_file_hashing(self, file_path : str, algorithm_name : str) -> str:
        """ Performs file hashing using different algorithms """
        
        BUF_SIZE = 4096

        algorithm_name = algorithm_name.lower() if algorithm_name.lower() in hashlib.algorithms_available else 'sha256'
        algorithm = hashlib.new(algorithm_name)
        
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                algorithm.update(data)


        return algorithm.hexdigest(64) if 'shake' in algorithm_name else algorithm.hexdigest()
