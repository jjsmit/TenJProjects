" basic highlighting
syntax on

set tabstop=4 softtabstop=4
set shiftwidth=4

" automatic indenting
set smartindent

" line nubers
set nu

" no text wrapping
set nowrap

" smartcase searching
set ignorecase
set smartcase

" dont create swapfiles
"set noswapfile
"set nobackup
"set undodir=~/.vim/undodir
"set undofile

" highlight searches
set incsearch

"set colorcolumn=80
"highlight ColorColumn ctermbg=0 guibg=lightgray

" pulgin manager -> plugin install location
call plug#begin('~/AppData/Local/nvim/plugged')

Plug 'morhetz/gruvbox'
Plug 'ycm-core/YouCompleteMe'

call plug#end()

colorscheme gruvbox
set background=dark
