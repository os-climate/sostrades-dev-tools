Welcome to sostrades-dev-tools documentation!
================================================

.. note::

   This project is under active development.

Objective
---------

The objective of this repository is to provide scripts to easily set up a working local environment.
It contains script facilities to clone repositories, and create virtual environments (using conda) for sostrades project.

The scripts clone the repositories in the correct folder for the rest of the scripts to work properly, as explained in Installation section.
The expected folder organisation is the following :

::

   ├── sostrades-dev-tools
   │   ├── dockers
   │   │   └── docker related files
   │   ├── models
   │   │   ├── sostrades-optimization-plugins
   │   │   ├── witness-core
   │   │   ├── witness-energy
   │   │   └── Other model repositories
   │   ├── platform
   │   │   ├── sostrades-core
   │   │   ├── sostrades-webapi
   │   │   ├── sostrades-webgui
   │   │   └── sostrades-ontology
   └── other files...

You are then free to change branches, pull changes, clone new model repositories and use scripts at your convenience.

Contents
--------
.. toctree::
   :hidden:

   Home <self>

.. toctree::

   Installation <installation.md>
   Linux Installation <linux-installation.md>
   Add personal repository <add-repository.md>
   User manual <user_manual.md>
   Developer manual <developer_manual.md>
   Release notes <release-notes.md>

.. _license:

License
=======

The content of this documentation is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.
