import zbar
import datetime


class Board(object):
    def __init__(self, board_id, cards):
        self.board_id = board_id
        self.cards = cards
        now = datetime.datetime.now()
        self.date = now.strftime("%Y-%m-%d_%H-%M-%S")

    def export_json(self, path):
        board_dict = {}
        board_dict['board'] = {}
        board_info_dict = dict(board_id=self.board_id, date=self.date)
        board_dict['board']['info'] = board_info_dict
        board_informations_dict = {}
        for card in self.cards:
            information_dict = dict(data=card.data, column=card.column)
            board_informations_dict[self.cards.index(card)] = information_dict
        board_dict['board']['informations'] = board_informations_dict

        #generate filename
        filename = "%s_%s.json" % (self.date, self.board_id)
        # write xml doc to file
        file = open(path + filename, "w")
        file.write(str(board_dict))
        file.close()
