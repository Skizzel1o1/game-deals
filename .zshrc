# Starship prompt
eval "$(starship init zsh)"

# Plugins laden
source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh

# Aliassen
alias ls="eza --icons --group-directories-first"
alias ll="eza -la --icons --group-directories-first"
alias top="htop"
alias matrix="cmatrix -b -C green"

# Systeeminfo bij opstarten
fastfetch
