import unittest

from src import datafile


class DatafileTest(unittest.TestCase):

    SOME_NAME = '/test/test'
    SOME_CTIME = '2011-11-12 23:23:23'

    def test_constructor(self):
        name = self.SOME_NAME
        ctime = self.SOME_CTIME
        dataFile = datafile.Datafile(name, ctime)

        self.assertTrue(name == dataFile.name, 'Error set name in constructor')
        self.assertTrue(ctime == dataFile.ctime, 'Error set cdate in constructor')

    def test_eq_with_name_and_ctime_are_equal_is_true(self):
        name = self.SOME_NAME
        ctime = self.SOME_CTIME
        dateFileA = datafile.Datafile(name, ctime)
        dateFileB = datafile.Datafile(name, ctime)
        self.assertTrue(dateFileA == dateFileB, 'Error comparing with __eq__')

    def test_eq_with_name_is_equal_and_ctime_is_not_equal_false(self):
        name = self.SOME_NAME
        ctimeA = self.SOME_CTIME
        ctimeB = '2011-11-12 23:23:24'
        dateFileA = datafile.Datafile(name, ctimeA)
        dateFileB = datafile.Datafile(name, ctimeB)
        self.assertFalse(dateFileA == dateFileB, 'Error comparing with __eq__')

    def test_eq_with_name_is_not_equal_and_ctime_not_equal_false(self):
        nameA = self.SOME_NAME
        ctime = self.SOME_CTIME
        nameB = nameA + 'im_so_different'
        dateFileA = datafile.Datafile(nameA, ctime)
        dateFileB = datafile.Datafile(nameB, ctime)
        self.assertFalse(dateFileA == dateFileB, 'Error comparing with __eq__')
