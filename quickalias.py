#!/usr/bin/env python3
"""
This simple python script creates permenant aliases so you don't have to open your shell config file
"""
import os
import sys
import subprocess
import argparse


class QuickAlias:
    """
    Creates permenant aliases
    """

    def __init__(self):
        pass

    def detect_shell(self) -> str:
        """ Detects the process calling the script """
        return (os.readlink(f'/proc/{os.getppid()}/exe') or os.environ.get("shell") or
                os.environ.get("SHELL"))

    def get_home_dir(self) -> str:
        """ Returns the home directory of the user """
        return os.environ.get("HOME") or os.environ.get("home") or os.path.expanduser('~')

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
        elif "tcsh" in shell:
            shell_config_path: str = os.path.join(home, '.tcshrc')
        elif "oh" in shell:
            shell_config_path: str = os.path.expanduser(os.environ.get(
                "OH_RC")) or os.path.join(home, '.oh-rc')
        else:
            # If the shell is not detected, it will default to fish.
            print("shell not detected. Defaulting to bash.")
            shell_config_path: str = None

        return shell_config_path

    def generate_alias_command(self, alias: str, command: str, shell: str):
        """ Generates the alias command """
        if "bash" in shell or "zsh" in shell or "ksh" in shell:
            alias_command: str = f"alias {alias}=\"{command}\""
        elif "tcsh" in shell:
            alias_command: str = f"alias {alias} \"{command}\""
        elif "oh" in shell:
            alias_command: str = "define " + \
                f"{alias}: method ((args)) " + \
                "{\n"+f"{command} (splice $args)\n"+"}"
        elif "fish" in shell:
            return ["fish", "-c", f"alias --save {alias} \"{command}\""]
        return alias_command

    def write_alias(self, alias_command: str, config_file: str) -> any:
        """ Writes the alias command to the config file """

        if os.path.isdir(config_file):
            return -2
        if os.path.exists(config_file):
            with open(config_file, encoding="utf-8") as file:
                if alias_command in file.read():
                    return -1

        with open(config_file, 'w', encoding="utf-8") as file:
            file.write(f"{alias_command}\n")
        return 0


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

    # Getting the desired alias and command.
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

    # Getting the path of the shell config file.
    shell_config: str = quickalias.get_shell_config_file(
        shell, user_directory)

    if shell_config is None:
        shell: str = "bash"
        shell_config: str = f"{user_directory}/.bashrc"

    if "fish" in shell:

        # Running the fish shell with the `-c` flag, which allows you to run a command in the shell.
        alias_command: str = quickalias.generate_alias_command(
            alias, command, shell
        )

        subprocess.run(alias_command, check=True, stdout=subprocess.DEVNULL)
        print(f"Ran command \"fish -c alias --save {alias} \"{command}\"\"")

    else:

        # generating the alias command.
        alias_string: str = quickalias.generate_alias_command(
            alias, command, shell)

        # Writing the alias to the config file.
        alias_written: int = quickalias.write_alias(alias_string, shell_config)

        # if alias already exists, it will exit.
        if alias_written == -1:
            print(f"\n{alias} already exists in {shell_config}",
                  file=sys.stderr)
            return 0

        if alias_written == -2:
            print(f"\n{shell_config} is a directory", file=sys.stderr)
            return 1


        print(f"\nAdded \"{alias_string}\" to shell config")

    source_command: str = f"source {shell_config}"
    print(f"You can source the new changes with:\n\t{source_command}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
