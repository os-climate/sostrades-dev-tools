# Release notes

The proper versioning and release of SoSTrades has started with the version 4.0.0.
## Release v5.3.0
Date: 2025-06-18

### Features

#### New Dashboard feature
A new Dashboard feature is now available. A dashboard can be created with study charts, texts and charts section. See the user manual for more information.

#### Import/ Export study
There is now the possibility to export a study in zip format and to import this study zip to create a study in stand-alone mode. A study in stand-alone mode is not editable and independant from any model source code change. This way, a study can be imported cross platform.
See the user manual for more information.

The study read-only files are saved in a new folder location and a migration script is run with the "init_process" flask command.

#### Core
- fix gather monoscenario outputs when outputs are nested types
- in dataset import/export, fix variables that have a point in short name
- variable parameter visibility removed to specified if a variable is 'shared', now there is only need to set a namespace to tell if a variable is shared.


### Library version upgrades
- pytest-cov from 5.0.0 to 6.2.0
- pytest-xdist from 3.6.1 to 3.7.0
- pytest-durations from 1.2.0 to 1.5.2
- ruff from 0.6.8 to 0.11.13
- pyarrow from 16.1.0 to 20.0.0
- PyYAML from 6.0.1 to 6.0.2
- openturns from 1.23 to 1.24
- black from 24.4.2 to 25.1.0
- chaospy from 4.3.15 to 4.3.18
- cma from 2.7.0 to 4.2.0
- cvxpy from 1.5.2 to 1.6.6
- gitpython from 3.1.43 to 3.1.44
- pycryptodome from 3.20.0 to 3.23.0
- six from 1.16.0 to 1.17.0
- psutil from 6.0.0 to 7.0.0
- PyJWT from 2.8.0 to 2.10.1
- python-dotenv from 1.0.1 to 1.1.0
- python3-saml from 1.9.0 to 1.16.0
- urllib3 from 2.2.2 to 2.3.0
- click from 8.1.7 to 8.2.1
- eventlet from 0.39.1 to 0.40.0
- furl from 2.1.3 to 2.1.4
- python-keycloak from 5.1.1 to 5.5.1
- pytz from 2024.1 to 2025.2
- requests from 2.32.3 to 2.32.4
- simplejson from 3.19.2 to 3.20.1


## Release v5.2.0
Date: 2025-04-15

### Features

#### PYTHON 3.12 UPDATE
Migrate from python 3.9 to python 3.12

#### Important Upgrade Information for python 3.12
To upgrade your local installation to python 3.12 :
- Clone or pull new version of platforms repository
- Remove .env folder
- Run PrepareVenv.py script (it will recreate venv with python 3.12)

#### Graphical User Interface (GUI)

* New fullscreen mode
* Donuts chart
* Button to switch to Read-Only Mode from Editon Mode

### Library version upgrades

* numpy from 1.24.4 to 1.26.4

#### Bug Fixes
- Buxfixes ReadOnly Mode loading
- xmlsec version
- Ontology discipline import issues

## Release v5.1.1
Date: 2025-18-03

### Features
This release is a hotfix release embedding the following bugfixes.

#### Bug Fixes
- Fixed verison for xmlsec to prevent docker build errors
- Use 0.39.1 release of eventlet to embed hotfix of queue typing
- Bugfix for command update readonly mode diagrams
- Bugfix for study active at pod start
- Bugfix for version.info

## Release v5.1.0
Date: 2025-03-10

### Features

#### Core
- Datasets:
  - BigQuery connector, Arango connector and SoSPickle connector are removed from available open source connectors.
  - New way to register a connector : connector_type is now the module path.
  - Support of Datasets connectors registration for local installation
    ##### Important Upgrade Information for v5.1.0
    - To upgrade to version 5.1.0, you must update your dataset connectors configuration in the sostrades-core `sostrades-core\sostrades_core\datasets\datasets_connectors\sample_connectors.json` file. 
    - If you wish to maintain your dataset connectors connectivity, follow these steps:
    1. Locate your connectors module path.
    2. Update the type according to the new format shown below.
        ###### Old format (pre v5.1.0)
        ```json
        [
          {
            "connector_id": "json_datasets_connector",
            "connector_type": "JSON",
            "connector_args": {
              "file_path": "./sostrades_core/tests/data/test_92_datasets_db.json"
            }
          },
          {
            "connector_id": "local_datasets_connector",
            "connector_type": "Local",
            "connector_args": {
              "root_directory_path": "./sostrades_core/tests/data/local_datasets_db/"
            }
          },
          {
            "connector_id": "json_V1_datasets_connector_for_witness_coarse_dev",
            "connector_type": "JSON_V1",
            "connector_args": {
              "file_path": "../../models/witness-core/climateeconomics/test/data/datasets/witness_coarse_dev_storytelling_test_dataset_db.json"
            }
          },
          {
            "connector_id": "local_V1_datasets_connector_for_witness_coarse_dev",
            "connector_type": "Local_V1",
            "connector_args": {
              "root_directory_path": "../../models/witness-core/climateeconomics/test/data/datasets/local_datasets_db/"
            }
          }
        ]
        ```
          
        ###### v5.1.0 Format
        ```json
        [
          {
            "connector_id": "json_datasets_connector",
            "connector_type": "sostrades_core.datasets.datasets_connectors.JSON_V0",
            "connector_args": {
              "file_path": "./sostrades_core/tests/data/test_92_datasets_db.json"
            }
          },
          {
            "connector_id": "local_datasets_connector",
            "connector_type": "sostrades_core.datasets.datasets_connectors.Local_V0",
            "connector_args": {
              "root_directory_path": "./sostrades_core/tests/data/local_datasets_db/"
            }
          },
          {
            "connector_id": "json_V1_datasets_connector_for_witness_coarse_dev",
            "connector_type": "sostrades_core.datasets.datasets_connectors.JSON_V1",
            "connector_args": {
              "file_path": "../../models/witness-core/climateeconomics/test/data/datasets/witness_coarse_dev_storytelling_test_dataset_db.json"
            }
          },
          {
            "connector_id": "local_V1_datasets_connector_for_witness_coarse_dev",
            "connector_type": "sostrades_core.datasets.datasets_connectors.Local_V1",
            "connector_args": {
              "root_directory_path": "../../models/witness-core/climateeconomics/test/data/datasets/local_datasets_db/"
            }
          }
        ]
      ```
- Core: New possibility to have display names in archi builders.

#### API/ User interface
- A study pod is no more needed to open a study in read-only mode. It mainly improve the study opening performances. 
  ##### Important Upgrade Information for v5.1.0 on your local installation
    - To upgrade to version 5.1.0, and still see visualization diagrams of your existing studies, you can update your already created studies read only mode by running the flask command `update_read_only_files_with_visualization`. 
    ```
    flask update_read_only_files_with_visualization
    ```

#### Bug Fixes
- Fix Petsc error when loading gemseo addons when there is no PETSC environment variable.

#### Local installation
- updated Developer Manual on ReadTheDoc

## Release v5.0.2
Date: 2025-02-14

### Features

#### API
* Keycloak authorization:
  - Platform authorization access is conditioned to the permissions to access the 'Default resource'
* Add study loading at pod start

#### Graphical User Interface (GUI)
* Update Angular version from 15 to 16
* Fix error/warning lint
* Charts:
  - Have a new chart section 'Key charts'
  - Charts are no more ordered by alphabetical order.
* Treeview: show the path to the discipline in error

#### Core
* Datasets:
  - Have local repository connector available in V1
* Fixed the double execution of MDA + driver + MDA

#### Local installation
* Local installation improvements
    - use uv instead of pip
* Fix minor bugs on windows/linux installation

## Release v5.0.1
Date: 2025-01-21

### Features

#### Local installation
- Local installation improvements
    - Added script to start local platform with a small GUI
- Installation documentation improvements
    - Separated Docker installation procedure
    - Improved wording and organisation of installation pages
    - Improved documentation of new repository addition

#### Core
- Run gemseo script (MDO & MDA) into SoStrades

#### Graphical User Interface (GUI)
- Fix Download study data button and move it into the opened study treeview

#### Other
- Add pre-commit hook

### Bug fixes
- Local Installation script issues fixes
- SQLite driver foreign key handling activated
- Minor fixes on GEMSEO compatibility

### Library version upgrades
* python-keycloak from 4.2.0 to 5.1.1

## Release v5.0.0
Date: 2024-12-19

### Features

#### Major Upgrade to GEMSEO v6.0.0
  - Update installation of GEMSEO as a library.
  - Native GEMSEO handling of former SoSTrades capabilities (Automatic MDA pre-run).
  - Rename variables on SoSTrades in coherence with GEMSEO.
  - Extensive bug-fixing.
  - More robust handling of data (types, exceptions) and algorithm options (pydantic models).
  - Refer to https://gemseo.readthedocs.io/en/stable/software/upgrading.html
  - Small memory increase due to GEMSEO known issue.

#### Bug Fixes
- Fixed error display in markdown documentation on GUI

#### Local Installation
- Improvement of Linux local installation


## Release v4.2.0
Date: 2024-11-21

### Features

#### Graphical User Interface (GUI)
- Added search bar functionality to export/import dataset notifications

#### Core
- Implemented the ability to specify custom colors for bar plots

#### API
- Integrated Keycloak provider to handle user authentication
- Support of SQLite for local installation
    ### Important Upgrade Information for v4.2.0
    - To upgrade to version 4.2.0, you must update your database configuration in the sostrades-webapi `configuration.json` file. 
    - If you wish to maintain connectivity with your existing MySQL database, follow these steps:
    1. Locate the `SQL_ALCHEMY_DATABASE` and `LOGGING_DATABASE` sections in your configuration file.
    2. Update these sections according to the new format shown below.
        #### Old format (pre v4.2.0)
        ```json
          "SQL_ALCHEMY_DATABASE": {
            "HOST" : "127.0.0.1",
            "PORT" : 3306,
            "USER_ENV_VAR": "SQL_ACCOUNT",
            "PASSWORD_ENV_VAR": "SQL_PASSWORD",
            "DATABASE_NAME": "sostrades-data",
              "SSL": false
          },
          "SQLALCHEMY_TRACK_MODIFICATIONS": false,
          "LOGGING_DATABASE": {
            "HOST" : "127.0.0.1",
            "PORT" : 3306,
            "USER_ENV_VAR": "LOG_USER",
            "PASSWORD_ENV_VAR": "LOG_PASSWORD",
            "DATABASE_NAME": "sostrades-log",
            "SSL": false
          },
        ```
          
        ### v4.2.0 Format
        ```json
            "SQL_ALCHEMY_DATABASE": {
                "ENGINE_OPTIONS": {
                    "pool_size":10,
                    "pool_recycle":7200
                },
                "CONNECT_ARGS": {
                    "ssl": false,
                    "charset": "utf8mb4"
                },
                "URI":"mysql+mysqldb://{USER}:{PASSWORD}@127.0.0.1:3306/sostrades-data",
                "URI_ENV_VARS": {
                    "USER": "SQL_ACCOUNT",
                    "PASSWORD": "SQL_PASSWORD"
                }
            },
            "SQLALCHEMY_TRACK_MODIFICATIONS": false,
            "LOGGING_DATABASE": {
                "ENGINE_OPTIONS": {
                    "pool_size":10,
                    "pool_recycle":7200
                },
                "CONNECT_ARGS": {
                    "ssl": false,
                    "charset": "utf8mb4"
                },
                "URI":"mysql+mysqldb://{USER}:{PASSWORD}@127.0.0.1:3306/sostrades-log",
                "URI_ENV_VARS": {
                    "USER": "LOG_USER",
                    "PASSWORD": "LOG_PASSWORD"
                }
            },
        ```

#### Bug Fixes
- Resolved an error that occurred during ontology installation on local Windows setups

#### Testing

- End-to-end tests (E2E)
  - Added new test cases for authentication with Keycloak

## Release v4.1.3
Date: 2024-10-24

### Features

#### Graphical User Interface (GUI)
- Added functionality to download documentation as PDF
- Implemented new loading page when opening a study
- Enabled study creation from the reference management page
- Unified common page for flavor editing across pages study_management, reference_management, and study_workspace
- Added study ID tooltip on hover over study name
- Consolidated dataset information into a single "Dataset_id" column on the dataset notification page
- Added possibility to retrieve documentation directly from files instead of ontology
- Renamed tabs in the study_workspace page

#### Core
- Introduced new versioning system for datasets:
  - V0: Legacy dataset mapping
  - V1: Added group handling for datasets
- Enhanced error handling for datasets

#### API
- Updated watcher for pod allocation
- Implemented study activity status verification

#### Bug Fixes
- Fixed error display during visualization-coupling-graph loading
- Implemented Git info reload after each click
- Resolved duplicate post-processing issue
- Added "stop study execution" notification for co-editing
- Implemented duplicate study name check before pod loading during creation
- Implemented waiting for "Ready" status from Kubernetes to ensure pod creation before opening a study
- Fixed "show legend" option on plots for charts

#### Testing
- Unit tests (L0 core)
  - Implemented tests for datasets with groups

- End-to-end tests (E2E)
  - Added tests for study creation from references
  - Implemented tests for flavor editing

## Release v4.1.2
Date: 2024-09-05

### Features
* GUI: Add a button on dataset import/export notification changes to export a CSV with data changes information (including path to dataset data)
This comes with the following changes:
- Database: new database migration (need to do a "flask db upgrade" command) to add 2 new columns to the StudyParameterChange table
- Datasets: Add function build_path_to_data that return the path/link/uri to retrieve the data in the dataset
* GUI: Hide dashboard page
* Sostrades-core: improve test gradient strategy
* Flavors configuration: sort flavors list by memory request and limit.
* Remove all coedition users at pod start (after the clean of all study pod allocation)

## Release v4.1.1 
Date: 2024-08-27

### Features
* Post-processings: add search bar in filters
* Post-processings section: save user section opened
* Datasets in Bigquery: add index sorting to keep dataframes order
* GUI header: display github repositories info with commits and tags
* GUI data management: limit the display of data size over 2Mo and limit data upload to 50Mo.
* API: Study API has the same image than the main Data API.
* Ontology: Added profiling and upgraded performances of ontology computation

### Bug fixes
* Fix Post-processings update when several disciplines at one node.
* Fix display icon for metrics in execution Logs

### Other
* Files reformatted with ruff checks

### Library version upgrades
* matplotlib from 3.9.0 to 3.9.2
* openturns from 1.18 to 1.23
* plotly from 5.3.0 to 5.22.0
* sympy from 1.9 to 1.13.0
* pytest from 7.4.3 to 8.1.2
* pytest-cov from 4.1.0 to 5.0.0
* pytest-xdist from 3.4.0 to 3.6.1
* flask from 1.1.1 to 2.3.3
* flask-jwt-extended from 3.24.1 to 4.6.0
* flask-migrate from 2.5.2 to 4.0.7
* flask-SQLAlchemy from 2.4.1 to 2.5.1
* SQLAlchemy from 1.3.13 to 1.4.52
* graphviz from 0.16 to 0.20.3
* jinja2 from 3.0.1 to 3.1.4
* PyJWT from 1.7.1 to 2.8.0
* werkzeug from 2.0.3 to 2.3.8

### GUI Library version upgrades
* Plotly to 2.23
* Changed markdown library from markdown-it to ngx-markdown
* Katex from 0.13 to 0.16
* Removed karma library

### Requirements added
* ngx-markdown (15.1.2) (GUI)
* google-cloud-bigquery-storage (2.25.0)
* eventlet: 0.36.1

## Release v4.1.0 
Date: 2024-07-15

### Compatibility notice
* Separation of sostrades-optimization-plugins module from platform core: add repository [https://github.com/os-climate/sostrades-optimization-plugins](https://github.com/os-climate/sostrades-optimization-plugins) for WITNESS optimization processes to continue functioning

### Features
* Datasets: wildcards generalized, parameter-level mapping, metadata
* Datasets in Bigquery: import, export, column name compatibility
* Post-processing sections
* Test speed-up: partial testing of use cases to avoid duplicates

### Bug fixes
* Pod execution metrics display on GUI (GB/GiB unit)
* Output retrieval mechanism for nested multi-scenarios
* Spurious double configuration of multi-instance disciplines

### Other
* Pre-commit and improved ruff checks (in DevOps)

### Library version upgrades
* tqdm from 4.61.0 to 4.66.4
* matplotlib from 3.4.3 to 3.9.0
* black from 22.12.0 to 24.4.2
* python-arango from 7.5.8 to 8.0.0
* cvxpy from 1.1.18 to 1.5.2 
* pycryptodome from 3.19.1 to 3.20.0
* sympy from 1.4 to 1.9
* requests from 2.31.0 to 2.32.3
* urllib3 from 2.1.0 to 2.2.2
* psutil from 5.9.5 to 6.0.0
* python-dotenv from 0.12.0 to 1.0.1
* python-keycloak from 4.0.0 to 4.2.0
* pytz from 2023.3.post1 to 2024.1 
* build-angular and angular cli from 15.2.10 to 15.2.11

### Requirements added
* ruff (0.5.0)
* google-cloud-bigquery (3.25.0)
* pyarrow (16.1.0)
* db-types (1.2.0)
* pycel (1.0b30)

## Release v4.0.2
Date: 2024-06-17

### Features

* Kubernetes watcher
* Datasets extended types in file system (import only)
* Ruff linting

### Bug fixes

* Documentation and visualisation tabs display
* Scrollbar on spreadsheet view
* Treeview display with multi-instance driver
* Avoid dump of empty cache
* Directory removal and creation

### Library version upgrades

* kubernetes (python library) from 11.0.0 to 29.0.0

## Release v4.0.1
Date: 2024-06-05

### Features

* Add Petsc garbage clean-up after Petsc execution
* Add option to deactivate postprocessing in MDODiscipline
* Clear jacobians after each end of MDO scenarios to improve memory performances
* New method get_datasets_database_mappings_folder_path to find the mapping folder path for a given repository name

### Bug fixes

* Add sparse matrices (lil_matrix) to initiate analytic gradients

### Library version upgrades

* chaospy from 4.3.7 to 4.3.15
* numpy from 1.23.3 to 1.24.4
* pandas from 2.2.1 to 2.2.2
* gitpython from 3.1.31 to 3.1.43
* jsonpickle from 3.0.2 to 3.0.4

## Release v4.0.0
Initial release

## Tagged Repositories

* [https://github.com/os-climate/sostrades-core](https://github.com/os-climate/sostrades-core)
* [https://github.com/os-climate/sostrades-webapi](https://github.com/os-climate/sostrades-webapi)
* [https://github.com/os-climate/sostrades-webgui](https://github.com/os-climate/sostrades-webgui)
* [https://github.com/os-climate/sostrades-ontology](https://github.com/os-climate/sostrades-ontology)
