import kanban
import json


class Mapper(object):
    def __init__(self, informations):
        self.informations = informations
        self.board_id = None
        self.columns_count = None
        self.read_config()
        self.columns = self.get_colums()

    def get_informations_starting_with(self, startsWith):
        matching_informations = []
        for information in self.informations:
            if information.data.startswith(startsWith):
                matching_informations.append(information)
        return matching_informations

    def read_config(self):
        config_codes = self.get_informations_starting_with('[')

        if len(config_codes) == 0:
            raise IOError('Klopfer says: No config code scanned!')

        config_code_data = config_codes[0].data
        config = json.loads(config_code_data)
        self.board_id = config[0]
        self.columns_count = config[1]

    def get_colums(self):
        columns = []
        column_informations = self.get_informations_starting_with('__')
        for information in column_informations:
            column = kanban.Column(None, information.location)
            columns.append(column)
        columns.sort(key=lambda Area: Area.center_x)
        last_column = None
        for column in columns:
            if not last_column == None:
                last_column.x_end = column.center_x
            column.id = columns.index(column)
            last_column = column
        if not last_column == None:
            columns.remove(last_column)

        if not self.columns_count == len(columns):
            raise IOError('Klopfer says: Scanned columns count != configured columns count!')

        return columns

    def get_cards(self):
        cards = []
        card_informations = self.get_informations_starting_with('T')
        for card_information in card_informations:
            card = kanban.Card(card_information.data, card_information.location)
            card.column = self.get_column_for_card(card)
            if card.column is not None:
                cards.append(card)
        return cards

    def get_column_for_card(self, card):
        for column in self.columns:
            if column.x_end > card.center_x and card.center_x > column.center_x:
                return column.id
        return None
