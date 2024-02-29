# Add personal repository

To add a personal repository after having already installed a sostrades local platform, you can follow the following steps.

## 1. Clone repository

Add your personal repository in the folder sostrades-dev-tools/models/<new repository>

## 2. Update conda env

Run the following command to update your conda environment from the folder sostrades-dev-tools/ by replacing <new repository> with your repository name in the command.
```
echo "$PWD/models/<new repository>" >> $(conda info --envs | awk -v env="SOSTradesEnv" '$0 ~ env {print $2 "/lib/python3.9/site-packages/conda.pth"}') 
```
Or you can edit the conda.pth file by yourself. You can find where the file is located with this command
```
conda info --envs | awk -v env="SOSTradesEnv" '$0 ~ env {print $2 "/lib/python3.9/site-packages/conda.pth"}'
```
Add the path of your repository at the end of the "conda.pth" file.

## 3. Update vscode settings.json file

Edit the sostrades-dev-tools/.vscode/settings.json file by adding your repository name at the end of python.analysis.extraPaths section
```
"python.analysis.extraPaths": [
        "./platform/gemseo/src",
        "./platform/sostrades-core",
        "./platform/sostrades-ontology",
        "./platform/sostrades-webapi",
        "./platform/sostrades-webgui",
        "./models/witness-core",
        "./models/witness-energy",
        "./models/<new repository>"
    ],
```

## 4. Rebuild Ontology (optional)  

If you want the ontology to take into account your new code, you need to re-build the ontology by running this command from sostrades-dev-tools folder
```
docker compose build ontology
```

## 5. Restart API and Ontology

Your new repository will be implemented in the platform after restarting API and Ontology. The best way is to run the two following commands
```
docker compose down
```
```
docker compose up
```
