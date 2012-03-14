import unittest
import os
from src import scanner


class ScannerTest(unittest.TestCase):
    def test_set_image(self):
        scan = scanner.Scanner('tests/test_board.jpg')
        self.assertTrue(scan.height == 500, 'error getting image height')   
        self.assertTrue(scan.width == 1500, 'error getting image width')

    def test_get_qr_code_size(self):
        scan = scanner.Scanner('tests/test_board.jpg')
        avg_qr_code_size = scan.get_qr_code_size()
        self.assertTrue(avg_qr_code_size == 42, 'error calculating qr code sizes')
  
    def test_scanner_works(self):
        scan = scanner.Scanner('tests/test_board.jpg')
        scan.scan()
        self.assertTrue(len(scan.symbols) == 13, 'error scanning all symbols')
