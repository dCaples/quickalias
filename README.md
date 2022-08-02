# Quickalias

This python script creates permanent aliases so you don't have to open your shell config file

*Dependencies:*

* python3

## Currently Supported Shells

* bash
* zsh
* fish
* ksh
* tcsh
* oh

## Installation

You have three ways to install this program.  

You can install with the pypi package (with pip):

```bash
pip install quickalias
```

You can install with the PKGBUILD (for Arch users):

```bash
git clone https://github.com/dCaples/quickalias
cd quickalias
makepkg -si
```

Or you can install with make:

```bash
git clone https://github.com/dCaples/quickalias
cd quickalias
sudo make install
```

## Usage

### Cli application

you may run `quickalias` in interactive mode:

> *This example is using the zsh shell*

  ```
  $ quickalias
  Enter alias for command: hello
  Enter the command: echo hello

  Added "alias hello="echo hello"" to shell config
You can source the new changes with:
      source /home/<user>/.zshrc
  ```

using flags:

> *This example is using the zsh shell*

  ```
  $ quickalias --alias "hello" --command "echo hello"

Added "alias hello="echo hello"" to shell config
You can source the new changes with:
        source /home/<user>/.zshrc
  ```

or using positional arguments:

> *This example is using the zsh shell*

  ```
  $ quickalias hello "echo hello"

Added "alias hello="echo hello"" to shell config
You can source the new changes with:
        source /home/<user>/.zshrc
  ```

#### Flags

| Flag              | Effect                                      |
|-------------------|---------------------------------------------|
| `-h` `--help`    | Display help information                     |
| `-a` `--alias`   | Provide the alias for the command            |
| `-c` `--commmand`| Provide the command to be aliased            |

### Python Module

Quickalias's main functions are avalible in other python programs as a module.  
An example program using this module:

```Python
# test.py

# Detecting the process calling the program

# Importing the module
import quickalias

# Initalizing the class
quickalias = quickalias.QuickAlias()

print(quickalias.detect_shell())
```

When running this program from a zsh shell it prints the following:

``` shell
$ python3 test.py
/usr/bin/zsh
```

The functions avalible in the module are the following:

* `detect_shell() -> str` - Returns the process calling the program
* `get_home_dir() -> str` - Returns the home directory of the user calling the function
* `get_shell_config_file(home: str) -> str` - Attempts to determine the config file for a provided shell.
* `generate_alias_command(alias: str, command: str, shell: str) -> any` - Take an alias and a command to be aliased and returns an alias command appropriate for the shell. *will return a list to be passed to subprocess.run if the shell is fish*
* `write_alias(alias_command: str, config_file: str) -> str` - Intended to write the output of `generate_alias_command()` to the location provided by `get_shell_config_file()`

## Contributing

* Check the issues (if there are any), it's a good place to start when you don't know what to do.
* Fork the repository and create pull requests to this repository.
* Don’t change the formatting; Dont reformat or otherwise change the formatting of source code or documentation in the repo. Use the same formatting as the rest of the codebase.
* Make documentation; If adding features or otherwise changing the user experience create documentation regarding the added or changed features.
* Use space only indentation in all source code files with the sole execption of `Makefile`. Do not use tabs or any form of indentation other than spaces. Use 4 space indentation.
