import hashlib

class HashAll:

    def __init__(self):
        pass

    def perform_hashing(self, text : str):
        
        results = {}

        for algorithm in sorted(hashlib.algorithms_available):
            obj = hashlib.new(algorithm)
            obj.update(text.encode('utf-8'))
            
            if 'shake' in algorithm:
                results[algorithm] = obj.hexdigest(64)
            else:
                results[algorithm] = obj.hexdigest()

        return results




