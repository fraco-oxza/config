call plug#begin(stdpath('data').'/plugged')
    " LANGUAGES
    " typescript
    Plug 'leafgarland/typescript-vim'
    " jsx in typescript
    Plug 'peitalin/vim-jsx-typescript'
    " fish
    Plug 'dag/vim-fish'
    " javascript
    Plug 'yuezk/vim-js'
    " jsx in javascrip
    Plug 'maxmellon/vim-jsx-pretty'
    " Rust 
    Plug 'rust-lang/rust.vim'
    " Toml
    Plug 'cespare/vim-toml'
    " Terraform
    Plug 'hashivim/vim-terraform'


    " Vim gutter
    Plug 'airblade/vim-gitgutter'

    " Molokai theme
    Plug 'arcticicestudio/nord-vim'

    "Vim fugitive
    Plug 'tpope/vim-fugitive'

    " icons for NERDTree
    Plug 'ryanoasis/vim-devicons'

    " NERDTree
    Plug 'preservim/nerdtree'

    " Conquer of completion
    Plug 'neoclide/coc.nvim', {'branch': 'release'}

    " Sorround
    Plug 'tpope/vim-surround'

    " Fzf 
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/fzf.vim'

    " Airline status bar
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'

    " Vim FloaTerm
    Plug 'voldikss/vim-floaterm'

    " NERDCommenter
    Plug 'preservim/nerdcommenter'

    " Html preview
    Plug 'turbio/bracey.vim'

    " Other themes
    Plug 'morhetz/gruvbox'


    " Subrrallador
    Plug 'norcalli/nvim-colorizer.lua'

    " Markdown preview
    Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }, 'for': ['markdown', 'vim-plug']}

call plug#end()
