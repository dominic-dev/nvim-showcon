import abc
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
        buffer_ = self.nvim.current.buffer
        directory = self.nvim.eval('getcwd()')
        directory = self.nvim.eval("expand('%:p:h')")
        extension = self.nvim.eval('expand("%:e")')

        class_name = extension.title() + 'Constructor'
        try:
            constructor_handler = globals()[class_name](extension, directory,\
                                                    current_word, self.nvim)
        except KeyError:
            message = "{} ({})".format(Constructor.NOT_SUPPORTED, extension)
        else:
            constructors = constructor_handler.get_constructors()
            message = " ## ".join(constructors)
        command = 'echom "{}"'.format(message)
        self.nvim.command(command)

    def _char_at(self, row, col):
        return self.nvim.current.buffer[row][col]


class Constructor:
    NOTHING_FOUND = "Nothing found."
    NOT_SUPPORTED = "This filetype is currently not supported."

    def __init__(self, language, directory, name, nvim):
        self._language = language
        self._directory = directory
        self._name = name
        self._nvim = nvim

    """
    Return list of constructors
    """
    @abc.abstractmethod
    def get_constructors(self):
        return

class JavaConstructor(Constructor):
    """
    Return java constructors
    """
    def __init__(self, language, directory, name, nvim):
        super().__init__(language, directory, name, nvim)

    """
    Return the file containing the constructor
    """
    def _get_constructor_file(self):
        os.chdir(self._directory)
        search_string = "{}/**/{}.{}".format(self._directory, self._name,\
                                             self._language)
        result = glob.glob(search_string, recursive=True)
        if(len(result) == 1):
            file_ = result[0]
        elif(len(result) > 1):
            choices = "\n&".join(["{}. {}".format(i+1, r) for i, r in enumerate(result)])
            self._nvim.command('call inputsave()')
            command = "let user_input = confirm('Choose a source', '&{}', 1)".format(choices)
            self._nvim.command(command)
            self._nvim.command('call inputrestore()')
            answer = self._nvim.eval('user_input')
            file_ = result[answer-1]
            self._nvim.command("echom '{}'".format(answer))
        else:
            file_ = None
        return file_

    def get_constructors(self):
        pattern = r".*public " + re.escape(self._name)
        prog = re.compile(pattern)
        constructors = []

        file_ = self._get_constructor_file();
        if (not file_):
            return [Constructor.NOTHING_FOUND]

        with open(file_) as f:
            for line in f.readlines():
                if (prog.match(line)):
                    # append stripped line
                    constructors.append(line.strip()[7:line.find("\{")])
        return constructors

