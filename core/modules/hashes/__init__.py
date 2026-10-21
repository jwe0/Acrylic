import hashlib

class hashes:
    def __init__(self):
        self.algos = {
            "md5": hashlib.md5,
            "sha1": hashlib.sha1,
            "sha224": hashlib.sha224,
            "sha256": hashlib.sha256,
            "sha384": hashlib.sha384,
            "sha512": hashlib.sha512,
            "sha3_224": hashlib.sha3_224,
            "sha3_256": hashlib.sha3_256,
            "sha3_384": hashlib.sha3_384,
            "sha3_512": hashlib.sha3_512,
            "shake_128": hashlib.shake_128,
            "shake_256": hashlib.shake_256,
            "blake2b": hashlib.blake2b,
            "blake2s": hashlib.blake2s,
        }

    def check_algorithm(self, algo):
        if algo not in self.algos:
            return False
        return True

    def run(self, algo, hash):

        hash_pw = self.algos[algo](
            hash.encode()
        ).hexdigest()

        return hash_pw