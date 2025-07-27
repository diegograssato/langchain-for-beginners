#!/bin/bash

# Remove the existing resolv.conf symlink
# This is necessary to avoid issues with DNS resolution in the container
sudo unlink /etc/resolv.conf

if [ -d .venv ]; then
    # If a virtual environment exists, activate it
    rm -rf .venv
fi

python3 -m venv .venv
source .venv/bin/activate

export PYTHONPATH=/workspaces/curso-langchain:$PYTHONPATH

# Use Google's public DNS server
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null
pip install --upgrade pip
pip install ipykernel

python -m ipykernel install --user --name langchain --display-name "Python (langchain)"
pip --disable-pip-version-check --no-cache-dir install -r  requirements.txt

#######
# Config ZSH
#######
# powerline fonts for zsh agnoster theme
git clone https://github.com/powerline/fonts.git --depth=1
cd fonts
./install.sh
cd .. && rm -rf fonts

# oh-my-zsh & plugins
zsh -c 'git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k'
cp -v .devcontainer/.p10k.zsh  ~/.p10k.zsh
cp -v .devcontainer/.zshrc ~/.zshrc
deactivate
