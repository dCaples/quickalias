# Quickalias

This python script creates permanent aliases so you don't have to open your shell config file

*Dependencies:*

* python3

## Installation

1. run the folowing to install:

```bash
sudo make install
```

## Usage

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

### Flags

| Flag              | Effect                                      |
|-------------------|---------------------------------------------|
| `-h` `--help`    | Display help information                     |
| `-a` `--alias`   | Provide the alias for the command            |
| `-c` `--commmand`| Provide the command to be aliased            |

## Contributing

* Check the issues (if there are any), it's a good place to start when you don't know what to do.
* Fork the repository and create pull requests to this repository.
* Don’t change the formatting; Dont reformat or otherwise change the formatting of source code or documentation in the repo. Use the same formatting as the rest of the codebase.
* Make documentation; If adding features or otherwise changing the user experience create documentation regarding the added or changed features.
* Use space only indentation in all source code files with the sole execption of `Makefile`. Do not use tabs or any form of indentation other than spaces. Use 4 space indentation.
