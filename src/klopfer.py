import directory
import scanner
import mapper
import board
import os


class Klopfer(object):
    def __init__(self, import_dir, export_dir):
        self.import_dir = import_dir
        self.export_dir = export_dir

    def run(self):
        # open dir and get oldest file with the given extension
        dir = directory.Directory(os, self.import_dir, ['jpg', 'jpeg'])
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
        current_board.export_json(self.export_dir)
