import unittest
import os
from mock import Mock
from src import directory
from src import datafile


class DirectoryTest(unittest.TestCase):
    def setUp(self):
        self.os = os
        self.directory = directory.Directory(self.os, 'test/', ['jpg'])

    def test_return_oldest_file(self):
        self._load_os_file_stubs(self._listdirValues(), self._ctimeValues())

        expected = datafile.Datafile('test/test.jpg', '2012-01-01 23:21:34')
        self.assertEquals(expected, self.directory.get_oldest_file())

    def test_return_oldest_file_given_some_more_files(self):
        listdirValues = self._listdirValues()
        listdirValues.append('test3.jpg')

        ctimeValues = self._ctimeValues()
        ctimeValues['test/test3.jpg'] = '2012-03-01 23:21:34'
        self._load_os_file_stubs(listdirValues, ctimeValues)

        expected = datafile.Datafile('test/test.jpg', '2012-01-01 23:21:34')
        self.assertEquals(expected, self.directory.get_oldest_file())

    def test_return_oldest_file_with_oldest_file_in_dir_does_not_match_filetypes(self):
        listdirValues = self._listdirValues()
        listdirValues.append('list.xml')

        ctimeValues = self._ctimeValues()

        self._load_os_file_stubs(listdirValues, ctimeValues)

        expected = datafile.Datafile('test/test.jpg', '2012-01-01 23:21:34')
        self.assertEquals(expected, self.directory.get_oldest_file())

    def test_return_oldest_file_ignore_upper_and_lower_filetypes(self):
        listdirValues = self._listdirValues()
        listdirValues.append('test3.JPG')

        ctimeValues = self._ctimeValues()
        ctimeValues['test/test3.JPG'] = '2009-03-01 23:21:34'
        self._load_os_file_stubs(listdirValues, ctimeValues)

        expected = datafile.Datafile('test/test3.JPG', '2009-03-01 23:21:34')
        self.assertEquals(expected, self.directory.get_oldest_file())

    def _load_os_file_stubs(self, listdirValues, ctimeValues):
        self.os.listdir = Mock(return_value = listdirValues)
        self.os.path.getctime = Mock(side_effect = lambda filename: ctimeValues[filename])

    def _listdirValues(self):
        return ['test2.jpg', 'test.jpg']

    def _ctimeValues(self):
        return {'test/test.jpg': '2012-01-01 23:21:34', 'test/test2.jpg': '2012-02-01 23:21:34'}
