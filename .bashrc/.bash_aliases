# Just because I prefer this over plain ls
alias ll="lsd -alFh"

# Zig
alias zb="zig build"
alias zbr="zig build -Doptimize=ReleaseSafe"
alias zt="zig test src/main.zig"

# Python virtual envs
alias ve="python3 -m venv ./venv"
alias vv="source ./venv/bin/activate"

# Flask
alias fr="flask run --host=0.0.0.0"

# Misc
alias myip="curl https://ip.mepley.net; echo"

# Use colored output where supported
alias ip="ip -color=auto"
alias grep="grep --color=auto"
