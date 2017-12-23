# Show Constructor

Thanks to /jacobsimpson/nvim-example-python-plugin for the neovim plugin template.


### Installation

Using <a href="https://github.com/Shougo/dein.vim">dein</a>
```Bash
    call dein#add('dominic-dev/show-constructor')
```

Using NeoBundle
```Bash
    NeoBundle 'dominic-dev/show-constructor'
```

### <a id="python_version"></a>Python Version

This plugin code works with Python 3.
```Python
pip3 install neovim
```

### Mapping 

Add this to your ~/.config/nvim/init.vim file
Replace ```<Leader\>s``` with your desired mapping

```VimL
nnoremap <silent> <Leader>s :exe "call ShowConstructor()"<CR>
```
