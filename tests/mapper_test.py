import unittest
from mock import Mock
from src import mapper


class MapperTest(unittest.TestCase):
    def setUp(self):
        self.symbols = []
        # columns
        self.columns_count = -1
        for i in range(0, 8, 1):
            symbol = Mock()
            symbol.location = ((0 + (7 - i) * 20, 0), ((7 - i) * 20, 10), (10 + (7 - i) * 20, 10), (10 + (7 - i) * 20, 0))
            symbol.data = "__"
            self.symbols.append(symbol)
            self.columns_count += 1
        # cards
        self.cards_count = 0
        for i in range(0, 7, 1):
            symbol = Mock()
            symbol.location = ((5 + i * 20, 5), (5 + i * 20, 15), (15 + i * 20, 15), (15 + i * 20, 5))
            symbol.data = "T" + str(i) * 5
            self.symbols.append(symbol)
            self.cards_count += 1
        # config symbol
        symbol = Mock()
        symbol.location = ((50, 50), (50, 60), (60, 60), (60, 50))
        self.board_id = 1
        symbol.data = "[%d,%d]" % (self.board_id, self.columns_count)
        self.symbols.append(symbol)

    def test_set_symbols(self):
        test_mapper = mapper.Mapper(self.symbols)
        self.assertEqual(self.symbols, test_mapper.informations)

    def test_get_board_id(self):
        test_mapper = mapper.Mapper(self.symbols)
        self.assertEqual(test_mapper.board_id, self.board_id)

    def test_get_colums_only(self):
        test_mapper = mapper.Mapper(self.symbols)
        columns = test_mapper.columns
        self.assertEqual(len(columns), self.columns_count)

    def test_get_colums_ordered(self):
        test_mapper = mapper.Mapper(self.symbols)
        columns = test_mapper.columns
        column_old = None
        for column in columns:
            if not column_old == None:
                self.assertTrue(column_old.center_x < column.center_x)
                self.assertTrue(column_old.id < column.id)
                self.assertTrue(column.x_end > column.center_x)
                self.assertEqual(column_old.x_end, column.center_x)
            column_old = column

    def test_scanned_columns_count_is_equal_to_config_column_count(self):
        symbols = []
        symbol = Mock()
        symbol.location = ((50, 50), (50, 60), (60, 60), (60, 50))
        columns_count = 1
        symbol.data = "[1,%d]" % (columns_count)
        symbols.append(symbol)
        self.assertRaises(IOError, mapper.Mapper, (symbols))

    def test_get_cards_only(self):
        test_mapper = mapper.Mapper(self.symbols)
        cards = test_mapper.get_cards()
        self.assertEqual(len(cards), self.cards_count)

    def test_column_for_card(self):
        test_mapper = mapper.Mapper(self.symbols)
        cards = test_mapper.get_cards()

        for card in cards:
            self.assertEqual(card.column, cards.index(card))
