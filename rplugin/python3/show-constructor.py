import neovim
import glob
import os
import re

@neovim.plugin
class Main(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function('ShowConstructor')
    def showConstructor(self, args):
        current_word = word = self.nvim.eval('expand("<cword>")')
        directory = self.nvim.eval('getcwd()')
        extension = self.nvim.eval('expand("%:e")')

        os.chdir(directory)
        search_string = "{}/**/{}.{}".format(directory, current_word, extension)
        result = glob.glob(search_string)
        found = 'no'
        f = None
        if(len(result) == 1):
            f = result[0]
            found = 'yes'
        if (not f):
            return

        c = Constructor(extension, f, current_word)
        constructors = c.get_constructors()

        message = " ## ".join(constructors)
        command = 'echom "{}"'.format(message)
        self.nvim.command(command)

        # command = 'echo "{}{}"'.format(current_word, directory)
        # self.nvim.command(command)


        # command = 'echo "{}"'.format(found)
        # self.nvim.command(command)

    def _char_at(self, row, col):
        return self.nvim.current.buffer[row][col]


class Constructor:
    def __init__(self, language, file_, name):
        self._language = language
        self._f = file_
        self.name = name

    """
    Return list of constructors
    """
    def get_constructors(self):
        return self.__getattribute__('_' + self._language)()

    """
    Return java constructors
    """
    def _java(self):
        pattern = "public " # + self.name + " ?\(.*\) ?\{"
        pattern = r"public "# + re.escape(self.name)# + r"\s?\(.*\)\s?u\{"
        pattern = r".*public " + re.escape(self.name)
        prog = re.compile(pattern)
        constructors = []

        with open(self._f) as f:
            for l in f.readlines():
                if (prog.match(l)):
                    #end = l.index(')')
                    # constructors.append(l.strip())
                    constructors.append(l.strip()[:l.find("\{")])
        return constructors

