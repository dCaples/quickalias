#!/usr/bin/env sh

python -m black ./quickalias.py || echo "Formatting failed, black is either not installed or unfindable."