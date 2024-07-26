# Release notes

The proper versioning and release of SoSTrades has started with the version 4.0.0.

<details open>
<summary><h2>Release v4.0.2</h2></summary>

## Features

* Kubernetes watcher
* Datasets extended types in file system (import only)
* Ruff linting (not mandatory in DevOps yet)

## Bug fixes

* Documentation and visualisation tabs display
* Scrollbar on spreadsheet view
* Treeview display with multi-instance driver
* Avoid dump of empty cache
* Directory removal and creation

## Library version upgrades

* kubernetes (python library) from 11.0.0 to 29.0.0
</details>

<details>
<summary><h2>Release v4.0.1</summary>

## Features

* Add Petsc garbage clean-up after Petsc execution
* Add option to deactivate postprocessing in MDODiscipline
* Clear jacobians after each end of MDO scenarios to improve memory performances
* New method get_datasets_database_mappings_folder_path to find the mapping folder path for a given repository name

## Bug fixes

* Add sparse matrices (lil_matrix) to initiate analytic gradients

## Library version upgrades

* chaospy from 4.3.7 to 4.3.15
* numpy from 1.23.3 to 1.24.4
* pandas from 2.2.1 to 2.2.2
* gitpython from 3.1.31 to 3.1.43
* jsonpickle from 3.0.2 to 3.0.4
</details>

## Tagged Repositories

* [https://github.com/os-climate/sostrades-core](https://github.com/os-climate/sostrades-core)
* [https://github.com/os-climate/sostrades-webapi](https://github.com/os-climate/sostrades-webapi)
* [https://github.com/os-climate/sostrades-webgui](https://github.com/os-climate/sostrades-webgui)
* [https://github.com/os-climate/sostrades-ontology](https://github.com/os-climate/sostrades-ontology)