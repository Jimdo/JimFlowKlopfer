import directory
import scanner
import mapper
import board
import os

dir = directory.Directory(os, '/home/michi/Apps/klopfer/photos/', ['jpg', 'jpeg'])
imagefile = dir.get_oldest_file()
scan = scanner.Scanner(imagefile.name)
informations = scan.scan()
mapping = mapper.Mapper(informations)
board_id = mapping.board_id
cards = mapping.get_cards()
current_board = board.Board(board_id, cards)
current_board.export_json('/home/michi/Desktop/')


