" Tabs And Spaces {{{

set tabstop=4 softtabstop=4
set shiftwidth=4

" }}}

" Backup and swapfiles {{{

" dont create swapfiles
"set noswapfile
"set nobackup
"set undodir=~/.vim/undodir
"set undofile

" }}}

" Searching {{{

set incsearch
set ignorecase
set smartcase

"}}}

" Plugins {{{

call plug#begin('~/AppData/Local/nvim/plugged')

Plug 'morhetz/gruvbox'
Plug 'ycm-core/YouCompleteMe'

call plug#end()

"}}}

" UI {{{

let mapLeader=" "
set smartindent
set relativenumber
set cursorline
set nowrap
syntax on
colorscheme gruvbox
set background=dark

"}}}

" VIMRC {{{

nnoremap <leader>ev :vsp $MYVIMRC<CR>
nnoremap <leader>sv :source $MYVIMRC <bar> :doautocmd BufRead<CR>

" }}}

" vim:foldmethod=marker:foldlevel=0
