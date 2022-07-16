#!/usr/bin/env sh

if [ ! -f "/usr/bin/python3" ]; then

  echo "no python3 found at '/usr/bin/python3'"
  exit 1
fi

install -Dm755 ./quickalias.py "$HOME/.local/bin/quickalias"
