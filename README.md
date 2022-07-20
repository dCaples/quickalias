# Quickalias

This python script creates permanent aliases so you don't have to open your shell config file

*Dependencies:*

* python3

## Install and setup

1. run the folowing to install:

```bash
sudo make install
```

2. run `quickalias` in interactive mode:

  ```
  $ quickalias
  Enter alias for command: hello
  Enter the command: echo hello

  Added "alias hello="echo hello"" to shell config
You can source the new changes with:
      source /home/<user>/.zshrc
  ```

or using arguments:

  ```
  $ quickalias --alias "hello" --command "echo hello"

Added "alias hello="echo hello"" to shell config
You can source the new changes with:
        source /home/<user>/.zshrc
  ```

3. Profit!!
