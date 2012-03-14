import directory
import scanner
import os

dir = directory.Directory(os, '/home/michi/Apps/klopfer/photos/', ['jpg', 'jpeg'])
imagefile = dir.get_oldest_file()
scan = scanner.Scanner(imagefile.name)
symbols = scan.scan()
board = board.Board(symbols)


