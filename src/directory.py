import datafile


class Directory(object):
    def __init__(self, os, path, filetypes):
        self.os = os
        self.path = path
        self.filetypes = filetypes

    def get_oldest_file(self):
        files = self.os.listdir(self.path)
        dataFiles = []
        for file in files:
            for filetype in self.filetypes:
                if file.lower().endswith(filetype.lower()):
                    imageFile = datafile.Datafile(self.path + file, self.os.path.getctime(self.path + file))
                    dataFiles.append(imageFile)

        dataFiles = sorted(dataFiles, key=lambda datafile: datafile.ctime)

        return dataFiles[0]
