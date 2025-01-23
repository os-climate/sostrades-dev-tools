# VS Code and Venv Tips

This page provides concise information about using Visual Studio Code (VS Code) and Python virtual environments (venv).

## Visual Studio Code (VS Code)

VS Code settings have been configured during the installation process using the `PrepareDevEnv` script.

To benefit from these settings, open the `sostrades-dev-tools` directory in VS Code by running the following command in the terminal:

```bash
code .
```

### Using venv in VS Code

1. Open the command palette by pressing `Ctrl + Shift + P`.
2. Search for "Python: Select Interpreter" and select it.

![Select Interpreter](images/select_interpreter.png)

3. Choose "Python 3.9.x ('.venv')".

![Select Python](images/select_python.png)

Now you can run any SoSTrades code from VS Code.

## Using venv

To activate the virtual environment with all the required packages installed, run the following command from the `sostrades-dev-tools` folder:

### Windows

```bash
.venv/Scripts/activate
```

### Linux

```bash
. .venv/bin/activate
```

To deactivate the virtual environment, use the following command:

```bash
deactivate
```
