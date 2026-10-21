import threading, time, datetime
from core.modules.logging import *
from core.modules.general import ascii_art, clear_screen
from core.modules.hashes import hashes

class Main:
    def __init__(self):
        clear_screen()
        ascii_art()
        self.hash = hashes()

        self.args = {
            "hash" : {
                "required" : True,
                "default"  : None
            },
            "algorithm" : {
                "required" : True,
                "default"  : None
            },
            "wordlist" : {
                "required" : False,
                "default"  : "core/dependencies/wordlist"
            }
        }
        self.config  = {}
        self.stats   = {}
        self.result  = ""
        self.start   = None
        self.end     = None
        self.found   = False
        self.checked = 0


    def get_args(self):
        for arg in self.args:
            arg_info = self.args[arg]

            required = arg_info["required"]
            default  = arg_info["default"]

            user_input = inpt(arg.title())

            while not user_input and required:
                error("Required argument")
                user_input = inpt(arg.title())

            if not user_input:
                user_input = default

            self.config[arg] = user_input


    def check(self, pw, hash, algorithm):
        hashed_ = self.hash.run(algorithm, pw)

        if hashed_.strip() == hash.strip():
            self.result = pw
            self.end = time.time()
            self.found = True

    def show_results(self):
        keys = list(self.stats.keys())
        vals = list(self.stats.values())

        key_pad = max([len(key) for key in keys])

        for i in range(len(keys)):
            msg = info(f"{keys[i]}{" " * (key_pad - len(keys[i]))} : {vals[i]}", False)
            print(msg)

    def run(self):
        if not self.hash.check_algorithm(self.config["algorithm"]):
            error("Unsupported hash algorithm")
            exit()

        algorithm = self.config["algorithm"]
        wordlist  = self.config["wordlist"]
        hash      = self.config["hash"]

        self.start = time.time()

        for pw in open(wordlist):
            self.checked += 1
            if self.found:

                break
            pw = pw.strip()

            threading.Thread(target=self.check, args=[pw, hash, algorithm]).start()

        if not self.found:
            error("Not found")
            exit()

        taken = int(self.end - self.start)

        print()
        success("Found")
        print()
        
        self.stats = {
            "original_hash" : hash,
            "algorithm"     : algorithm,
            "wordlist"      : wordlist,
            "checked"       : self.checked,
            "password"      : self.result,
            "taken"         : taken
        }
        


    def main(self):
        self.get_args()
        self.run()
        self.show_results()

if __name__ == "__main__":
    main = Main()
    main.main()