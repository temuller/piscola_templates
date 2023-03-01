#!/usr/bin/env python

import os
import shutil
import piscola
pisco_path = piscola.__path__[0]

# get template directories in current directory
template_dirs =[directory for directory in os.listdir('.') 
                if not directory.startswith('.') and os.path.isdir(directory)]

# copy the templates to your piscola installation path
for temp_dir in template_dirs:
    dest_dir = os.path.join(pisco_path, 'templates', temp_dir)
    shutil.copytree(temp_dir, dest_dir, dirs_exist_ok=True)
    print(f'{temp_dir} template copied to your local installation of PISCOLA')