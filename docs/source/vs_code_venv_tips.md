# VS Code and Venv tips
This page covers some information about VS code and python venv usage tips.

## Visual Studio Code (VSCode) 
VSCode settings have been written in dedicated files during installation (script `PrepareDevEnv`).

In order to benefit from VSCode settings, type the following command in the `sostrades-dev-tools` directory, at the same level than the `./vscode` (hidden) folder (or `models/` and `platform/` visible directories) :
```bash
code .
```

### Use venv in VS code

In VS Code, use keys ctrl + shift + p to open command panel, search for "Python: Select Interpreter"

![](images/select_interpreter.png) 

Select "Python 3.9.x (".venv")

![](images/select_python.png) 

Now you can launch any SoSTrades code from VSCode.


## Venv

To run .venv with all requirements installed, run the following command from your `sostrade-dev-tools` folder:

(Windows)
```bash
.venv/Scripts/activate
```
(Linux)
```bash
. .venv/bin/activate
```

To exit the venv just use this command

```
deactivate
```
