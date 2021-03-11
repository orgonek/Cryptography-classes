from hash_all import HashAll
import hashlib
import os

obj = HashAll()

path = os.path.join(os.path.expanduser('~'),'Downloads', 'ubuntu-20.04.2.0-desktop-amd64.iso')

print(obj.perform_file_hashing(path, 'sha256'))


