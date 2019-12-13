import random

random.seed(1234)

import atexit
import gc
import io
import os
import tempfile

TEST_DIR = tempfile.TemporaryDirectory()
atexit.register(TEST_DIR.cleanup)

OLD_CWD = os.getcwd()
atexit.register(lambda: os.chdir(OLD_CWD))


def close_open_files():
    everything = gc.get_objects()
    for obj in everything:
        if isinstance(obj, io.IOBase):
            obj.close()


atexit.register(close_open_files)

# Example 1
import sys

print(sys.version_info)
print(sys.version)
