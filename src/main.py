import directory
import scanner
import mapper
import board
import os
from sys import argv

import_dir = argv[1]
export_dir = argv[2]

if not os.path.isdir(import_dir):
    raise IOError('Klopfer says: import directory is not a directory')

if not os.path.isdir(export_dir):
    raise IOError('Klopfer says: export directory is not a directory')

# open dir and get oldest file with the given extension
dir = directory.Directory(os, import_dir, ['jpg', 'jpeg'])
imagefile = dir.get_oldest_file()

# open image
scan = scanner.Scanner(imagefile.name)
informations = scan.scan()

# remove old image
os.remove(imagefile.name)

# load board_id and cards
mapping = mapper.Mapper(informations)
board_id = mapping.board_id
cards = mapping.get_cards()

# create board
current_board = board.Board(board_id, cards)
# write baord to json
current_board.export_json(export_dir)
