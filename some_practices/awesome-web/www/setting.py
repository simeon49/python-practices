# -*- coding: utf-8 -*

import sys
import os
import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'polls.yaml'

def get_config(path):
    with open(path) as f:
        config = yaml.load(f)
    return config

config = get_config(config_path)

# 将当前根路径追加到库搜索库中
sys.path.append(os.path.abspath('.'))
