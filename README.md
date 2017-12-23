# Show Constructor

Thanks to /jacobsimpson/nvim-example-python-plugin for the neovim plugin template.


### Downloading and installing

```Bash
git clone https://github.com/dominic-dev/show-constructor.git ~/.vim/bundles/show-constructor/
rm -rf ~/.vim/bundles/show-contructor/.git
```

### <a id="configuring-vim"></a>Configuring Vim

I use NeoBundle so this is an example of how to load this plugin in NeoBundle.

```VimL
" Required:
call neobundle#begin(expand('~/.vim/bundle/'))

    " Let NeoBundle manage NeoBundle
    " Required:
    NeoBundleFetch 'Shougo/neobundle.vim'

    " You probably have a number of other plugins listed here.

    " Add this line
    NeoBundle 'show-constructor'
call neobundle#end()
```

### <a id="python_version"></a>Python Version

This plugin code works with Python 3.
```Python
pip3 install neovim
```

### <a id="initializing"></a>Initializing Vim with Remote Plugin

The next thing to do is to initialize the manifest for the Python part of the
plugin. The manifest is a cache that Vim keeps of the interface implemented by
the Python part of the plugin. The functions and commands it implements.

To initialize the manifest, execute:

```VimL
:UpdateRemotePlugins
```

**NOTE:** After initializing the manifest, you must restart neovim for the python
functions be be available.

### Mapping 

Add this to your ~/.config/nvim/init.vim file
Replace <Leader>s with your desired mapping

```VimL
nnoremap <silent> <Leader>s :exe "call ShowConstructor()"<CR>
```
