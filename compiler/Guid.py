import random
import hashlib

def gen_guid():
    num = f'{random.random()}'.encode('ascii')
    hashobj = hashlib.sha256(num)
    return hashobj.hexdigest()[:8]