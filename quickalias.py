#!/usr/bin/env python3
"""
This simple python script creates permenant aliases so you don't have to open your shell config file
"""
import os
import sys
import subprocess
import argparse


class QuickAlias:
    def __init__(self):
        pass

    def detect_shell(self) -> str:
        """ Detects the process calling the script """
        return os.environ.get("SHELL") or os.readlink(f'/proc/{os.getppid()}/exe')

    def get_home_dir(self) -> str:
        """ Returns the home directory of the user """
        return os.environ.get("HOME") or os.path.expanduser('~')

    def get_shell_config_file(self, shell: str, home: str) -> str:
        """ Returns the shell config file path """
        if "bash" in shell:
            # Getting the path of the bashrc.
            shell_config_path: str = os.path.join(home, '.bashrc')

        elif "zsh" in shell:

            # Getting the path of the .zshrc file.
            shell_config_path: str = os.path.join(
                os.environ.get('ZDOTDIR') or home, '.zshrc')
        elif "fish" in shell:

            # Getting the path of the config.fish file.
            shell_config_path: str = os.path.join(
                os.environ.get('XDG_CONFIG_HOME') or os.path.join(
                    home, '.config'), 'fish/config.fish')
        elif "ksh" in shell:
            # Getting the path of the .kshrc file.
            shell_config_path: str = os.environ.get(
                'ENV') or os.path.join(home, '.kshrc')
        else:
            # If the shell is not detected, it will default to fish.
            print("shell not detected. Defaulting to bash.")
            shell_config_path: str = None

        return shell_config_path


def main() -> int:
    """
    the main method
    """

    # Creating an instance of the class `QuickAlias`
    quickalias = QuickAlias()

    # Creating a description for the script and then creating a parser for the arguments.
    module_description: str = "This script creates pemenant aliases so you don't have to."
    parser = argparse.ArgumentParser(description=module_description)
    parser.add_argument(
        "-a", "--alias", help="the alias for the command", required=False)
    parser.add_argument('alias', nargs='?', default=argparse.SUPPRESS)
    parser.add_argument("-c", "--command",
                        help="the command to be aliased", required=False)
    parser.add_argument('command', nargs='?', default=argparse.SUPPRESS)
    args = parser.parse_args()

    if args.alias and args.command:
        alias: str = args.alias
        command: str = args.command
    else:
        # Asking the user to input the alias and the command.
        alias: str = input('Enter alias for command: ')
        command: str = input('Enter the command: ')

    # Getting the home directory of the user.
    user_directory: str = quickalias.get_home_dir()

    if user_directory == '':
        print('Could not find home directory', file=sys.stderr)
        return 1

    # Getting the process id of the parent process from proc.
    shell: str = quickalias.detect_shell()

    if shell == '':
        print('Could not detect shell', file=sys.stderr)
        return 1

    shell_config: str = quickalias.get_shell_config_file(
        shell, user_directory)

    if shell_config is None:
        shell: str = "bash"
        shell_config: str = f"{user_directory}/.bashrc"

    if "bash" in shell or "zsh" in shell:
        alias_string: str = f"alias {alias}=\"{command}\""
        print(alias_string)
        # This is checking if the alias already exists in the config file.
        # if it does, it will not add it again.
        with open(shell_config, encoding="utf-8") as file:
            if alias_string in file.read():
                print(f"\n{alias} already exists in {shell_config}",
                      file=sys.stderr)
                sys.exit(0)

        # Opening the config file in append mode and writing the alias to the file.
        with open(shell_config, 'a', encoding="utf-8") as file:
            file.write(f"{alias_string}\n")
    elif shell in "ksh":
        alias_string: str = f"alias {alias}=\"{command}\""

        # This is checking if the alias already exists in the config file.
        # if it does, it will not add it again.
        with open(shell_config, encoding="utf-8") as file:
            if alias_string in file.read():
                print(f"\n{alias} already exists in {shell_config}",
                      file=sys.stderr)
                sys.exit(0)

        # Opening the config file in append mode and writing the alias to the file.
        with open(shell_config, 'a', encoding="utf-8") as file:
            file.write(f"{alias_string}\n")

    elif "fish" in shell:
        # Running the fish shell with the `-c` flag, which allows you to run a command in the shell.
        subprocess.run(
            ["fish", "-c", f"alias --save {alias} \"{command}\""], check=True,
            stdout=subprocess.DEVNULL)
    else:
        print("Shell not detected, exiting.", file=sys.stderr)

    print(f"\nAdded \"{alias_string}\" to shell config")

    source_command: str = f"source {shell_config}"
    print(f"You can source the new changes with:\n\t{source_command}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
