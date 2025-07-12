#!/bin/bash
set -e

# Install pwndbg
if [ ! -d "pwndbg" ]; then
  git clone https://github.com/pwndbg/pwndbg
  cd pwndbg
  ./setup.sh
  cd ..
fi

# Install gef
if [ ! -d "$HOME/.gdbinit.d" ]; then
  mkdir -p ~/.gdbinit.d
  git clone https://github.com/hugsy/gef ~/.gdbinit.d/gef
  echo "source ~/.gdbinit.d/gef/gef.py" >> ~/.gdbinit
fi

echo "[+] CCE-ready environment initialized."
