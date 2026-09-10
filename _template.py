# systemcheck2026
# crushallhumans
# puzzle N
# 12/n/2026

import os
import re
import sys
import math
import unittest
import socket
import hashlib
import pprint
import random
import time
from functools import reduce
from functools import cache
from itertools import chain
from multiprocessing import Pool
pp = pprint.PrettyPrinter()

CHALLENGE_YEAR = '2026'
DEBUG = False
TEST_INPUT_STRING_ONE = """
"""
TEST_INPUT_STRING_TWO = TEST_INPUT_STRING_ONE
TEST_ONE_RESULT = 8888
TEST_TWO_RESULT = 7777


def reprocess_input(param_set):
    if isinstance(param_set,str):
        l = []
        l = [input_line.strip() for input_line in param_set.splitlines()]
        param_set = l
    return param_set    


def one_star(param_set, is_two_star = False):
    if not is_two_star: print("---------------one_star--------------------")
    param_set = reprocess_input(param_set)
    c = 8888
    for i in param_set:
        continue
    return c

def two_star(param_set):
    print("---------------two_star--------------------")
    #return one_star(param_set,True)
    param_set = reprocess_input(param_set)
    c = 7777
    for i in param_set:
        continue
    return c










#---------------------------------------------------------
def P(*args, force = False, end = "\n"):
    if DEBUG or force:
        if not len([*args]):
            print('')
        else:
            if len([*args]) > 1:
                if end:
                    print(' '.join(str(x) for x in [*args]),end = end)
                else:
                    pp.pprint([*args])
            else:
                print([*args][0],end = end)


class testCase(unittest.TestCase):
    global DEBUG
    DEBUG = True

    def test_one_star(self):
        self.assertEqual(
            one_star(TEST_INPUT_STRING_ONE),
            TEST_ONE_RESULT
        )

    def test_two_star(self):
        self.assertEqual(
            two_star(TEST_INPUT_STRING_TWO),
            TEST_TWO_RESULT
        )



if __name__ == '__main__':
    try:
        sys.argv[1]
        DEBUG = False

        username = 'crushing'
        challenge_path = 'Development/crushallhumans/adventofcode'
        m = hashlib.sha256()
        hostname = socket.gethostname()
        m.update(hostname.encode('utf8'))
        if (
            m.hexdigest() == 'ec7c98e2b47378ec88e1f9cce8d6ed91b9d616787c8a37023fd5c67cef1ff71f' or
            m.hexdigest() == '8d4305a1b8b8f9c0ca17cd8a6b7a4f8e708ed1552dc479922bc4bb03501489e8'
        ):
            username = 'conrad.rushing'
        challenge_path = 'toast/crushallhumans-repos/adventofcode'
        print ('hostname str :',hostname)
        print ('hostname hash:', m.hexdigest())

        filename_script = os.path.basename(__file__)
        print("---------------%s--------------------"%filename_script)
        filename = filename_script.split('.')[0]
        input_set = ()
        with open("/Users/%s/%s%s/inputs/%s.txt" % (username,challenge_path,CHALLENGE_YEAR,filename)) as input_file:
            input_set = reprocess_input(input_file.read())

        start = (time.time() * 1000)
        ret = one_star(input_set)
        print (ret)
        print ('elapsed:',(time.time() * 1000) - start,'ms')

        start = (time.time() * 1000)
        ret = two_star(input_set)
        print (ret)
        print ('elapsed:',(time.time() * 1000) - start,'ms')
    except Exception as e:
        print(e)
