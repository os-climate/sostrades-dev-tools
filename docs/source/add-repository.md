# Add personal repository

To add a personal repository after having already installed a sostrades local platform, you can follow the following steps.

## 1. Clone repository

Add your personal repository in the folder `sostrades-dev-tools/models/<new repository>`

## 2. Update venv

Edit the `./sostrades-dev-tools/.venv/Lib/site-packages/sostrades.pth` file.  
Add the path of your repository at the end of the `sostrades.pth` file.

## 3. Update vscode settings.json file

Edit the `sostrades-dev-tools/.vscode/settings.json` file by adding your repository name at the end of `python.analysis.extraPaths` section
```
"python.analysis.extraPaths": [
        "./platform/sostrades-core",
        "./platform/sostrades-ontology",
        "./platform/sostrades-webapi",
        "./platform/sostrades-webgui",
        "./models/sostrades-optimization-plugins",
        "./models/witness-core",
        "./models/witness-energy",
        "./models/<new repository>"
    ],
```

## 4. Rebuild Ontology (optional)  

If you want the ontology to take into account your new code, you need to re-build the ontology by running this command from `sostrades-dev-tools/` folder

### Using local platform installation
Run script `scripts/UpdateOntology.py` 

### Using docker
```
docker compose build ontology
```

## 5. Restart API and Ontology

Your new repository will be implemented in the platform after restarting API and Ontology.

### Using local platform installation
Close all terminals, and restart script `scripts/StartSoSTrades.py` 

### Using docker
Run the following commands:
```
docker compose down
```
```
docker compose up
```
