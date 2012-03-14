import unittest

from tests import directory_test
from tests import datafile_test
from tests import scanner_test
from tests import board_test
from tests import mapper_test


loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(directory_test)

suite.addTests(loader.loadTestsFromModule(datafile_test))
suite.addTests(loader.loadTestsFromModule(scanner_test))
suite.addTests(loader.loadTestsFromModule(board_test))
suite.addTests(loader.loadTestsFromModule(mapper_test))


runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
