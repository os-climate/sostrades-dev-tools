# Release notes

The proper versioning and release of SoSTrades has started with the version 4.0.0.

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
* Change markdown library from markdown-it to ngx-markdown
* katex from 0.13 to 0.16
* remove karma library

### Requirements added
* ngx-markdown (15.1.2) (GUI)
* google-cloud-bigquery-storage (2.25.0)
* eventlet: 0.36.1

## Release v4.1.0 
Date: 2024-07-15

### Compatibility notice
* Separation of sostrades-optimization-plugins module from platform core: add repository https://github.com/os-climate/sostrades-optimization-plugins for WITNESS optimization processes to continue functioning

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
* Ruff linting (not mandatory in DevOps yet)

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

### Tagged Repositories

* [https://github.com/os-climate/sostrades-core](https://github.com/os-climate/sostrades-core)
* [https://github.com/os-climate/sostrades-webapi](https://github.com/os-climate/sostrades-webapi)
* [https://github.com/os-climate/sostrades-webgui](https://github.com/os-climate/sostrades-webgui)
* [https://github.com/os-climate/sostrades-ontology](https://github.com/os-climate/sostrades-ontology)
