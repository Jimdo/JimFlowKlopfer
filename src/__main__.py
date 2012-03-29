import os
import klopfer
import scanner
from sys import argv

if argv[1] == '--debug':
    image_path = argv[2]
    scanner = scanner.Scanner(image_path)
    informations = scanner.scan()
    for information in informations:
        print 'data: ' + information.data + ' center_x: ' + str(information.center_x)
    
else:
    import_dir = argv[1]
    export_dir = argv[2]

    if not os.path.isdir(import_dir):
        print 'Klopfer says: import directory is not a directory'

    if not os.path.isdir(export_dir):
        print 'Klopfer says: export directory is not a directory'

    klopfer = klopfer.Klopfer(import_dir, export_dir)
    try:
        klopfer.run()
    except IOError as error:
        print error
        try:
            klopfer.remove_image()
        except:
            pass

            
