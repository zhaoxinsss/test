# -*- coding: utf-8 -*-
'''
项目管理和辅助工具
'''
#2019/03/28 QTAF自动生成

import sys
import os

proj_root = os.path.dirname(os.path.abspath(__file__))
if proj_root not in sys.path:
    sys.path.insert(0, proj_root)
exlib_dir = os.path.join(proj_root, 'unisinsight-commom-lib')
if os.path.isdir(exlib_dir):
    for filename in os.listdir(exlib_dir):
        if filename.endswith('.egg'):
            lib_path = os.path.join(exlib_dir, filename)
            if os.path.isfile(lib_path) and lib_path not in sys.path:
                sys.path.insert(0, lib_path)
            
from testbase.management import ManagementTools

if __name__ == '__main__':    
    ManagementTools().run()
