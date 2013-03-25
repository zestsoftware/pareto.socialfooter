#!/usr/bin/env python

"Adding cache headers for image files in a directory"

import glob
import os
file_names = []

# get all files in the directory with an image extension
for file_type in ['*.png','*.gif','*.jpg']:
    file_names.extend(glob.glob(file_type))

# create a files with '.metadata' added and fill them with the string in line 16
for file_name in file_names:
    file = open('%s.metadata' % file_name, 'w')
    file.write('[default]\ncache = HTTPCache')