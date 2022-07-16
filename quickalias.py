#!/usr/bin/env python3
"""
This simple python script creates pemenant aliases so you don't have to open your shell config file
"""
import os
import sys

# Getting the home directory of the user.
user_directory: str = os.path.expanduser('~')

# Getting the process id of the parent process.
process_id: str = os.readlink(f'/proc/{os.getppid()}/exe')

if "bash" in process_id:
    SHELL = "bash"
    # Getting the path of the bashrc.
    shell_config_path: str = os.path.join(user_directory, '.bashrc')

elif "zsh" in process_id:
    SHELL = "zsh"
    shell_config_path: str = os.path.join(user_directory, '.zshrc')
elif "fish" in process_id:
    SHELL = "fish"
    shell_config_path: str = os.path.join(
        user_directory, '.config/fish/config.fish')
else:
    SHELL = "fish"
    print("Shell not detected, using default shell (fish).")
    shell_config_path: str = None

if shell_config_path is not None:
    config_location: str = shell_config_path
else:
    config_location: str = f"{user_directory}/.config/fish/config.fish"

alias: str = input('enter alias for command: ')
command: str = input('enter the command: ')

if SHELL in "bash" or SHELL in "zsh":
    alias_string: str = f"alias {alias}=\"{command}\""

else:
    alias_string: str = f"alias {alias} \"{command}\""

with open(config_location, encoding="utf-8") as f:
    if alias_string in f.read():
        print(f"{alias} already exists in {config_location}")
        sys.exit(0)

with open(config_location, 'a', encoding="utf-8") as f:
    f.write(f"{alias_string}\n")

print(f"added \"{alias_string}\" to shell config")

source_command: str = f"source {config_location}"
print(f"You can source the new changes with:\n\t{source_command}")
