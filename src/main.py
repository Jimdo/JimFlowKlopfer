import os
import klopfer
from sys import argv

import_dir = argv[1]
export_dir = argv[2]

if not os.path.isdir(import_dir):
    raise IOError('Klopfer says: import directory is not a directory')

if not os.path.isdir(export_dir):
    raise IOError('Klopfer says: export directory is not a directory')

klopfer = klopfer.Klopfer(import_dir, export_dir)
klopfer.run()


