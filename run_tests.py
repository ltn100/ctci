import os
from pathlib import Path
import pytest

files = [
    str(path) for path in Path(os.path.dirname(os.path.realpath(__file__))).glob('**/*.py')
    if not str(path).endswith("x_y_name.py")
]
files.sort()

if __name__ == '__main__':
    print(files)
    pytest.main(args=files)
