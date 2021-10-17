" Change Work dir
nnoremap <leader>cd :cd %:p:h<cr>

" Mapping NERDTree
map <F2> :NERDTreeToggle<cr>

" Open Fzf
map <tab> :Files<cr>

" Configuration 
let g:floaterm_keymap_new    = '<F7>'
let g:floaterm_keymap_prev   = '<F5>'
let g:floaterm_keymap_next   = '<F6>'
let g:floaterm_keymap_toggle = '<F8>'

" NerdCommenter Toggle remap to CTRL+tab
vmap <M-tab> <Plug>NERDCommenterToggle<cr>
nmap <M-tab> <Plug>NERDCommenterToggle<cr>

" Snippets 
" Use <C-l> for trigger snippet expand.
imap <C-l> <Plug>(coc-snippets-expand)

" Use <C-j> for select text for visual placeholder of snippet.
vmap <C-j> <Plug>(coc-snippets-select)

" Use <C-j> for jump to next placeholder, it's default of coc.nvim
let g:coc_snippet_next = '<c-j>'

" Use <C-k> for jump to previous placeholder, it's default of coc.nvim
let g:coc_snippet_prev = '<c-k>'

" Use <C-j> for both expand and jump (make expand higher priority.)
imap <C-j> <Plug>(coc-snippets-expand-jump)

" Use <leader>x for convert visual selected code to snippet
xmap <leader>x  <Plug>(coc-convert-snippet)

" next buffer
nmap <C-l> :bn<cr>
vmap <C-l> :bn<cr>

" Previus buffer 
nmap <C-h> :bp<cr>
vmap <C-h> :bp<cr>

" Delete buffer 
nmap <C-k> :bd<cr>
vmap <C-k> :bd<cr>


