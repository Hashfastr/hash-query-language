import random
import hashlib

# The GUIDs we use throughout the end generation
# Are just a hash of the string of a random float, keeping the first 8 chars.
def gen_guid():
    num = f'{random.random()}'.encode('ascii')
    hashobj = hashlib.sha256(num)
    return hashobj.hexdigest()[:8]