# Developer Manual

This documentation manual is designed for people looking to develop their own models, processes or studies in SoSTrades, leveraging all extended capabilities of its execution and configuration engine. 

SoSTrades is a web-based, multi-user, interactive publication-quality graph simulation platform. It allows users to drop new modules without additional coding, and provides embedded advanced numerical capabilities for simulation and multi-disciplinary optimization.

Learn how to create a wrapper for one of your Python model, define your I/O variables, create your post-processings, combine wrapper in processes, configure your own studies with SoSTrades capabilities.


## Chapter 1: Overall Introduction
TBD
### Section 1.1: What is SoSTrades ? 
explain gemseo 
explain that it comes with a GUI, refers to the user manual
explain all benefits to use sostrades (instead of gemseo)
### Section 1.2: SoSTrades main concepts
explain what is a model/wrapp/process/study 
explain what is a MDA/MDO/DOE ...
explain what is a namespace (theorically)


## Chapter 2: How to wrap your model in SoSTrades ?  
TBD
### Section 2.1: Input/output variables definition
TBD
### Section 2.2: Run method
TBD
### Section 2.3: Post-processing definition
TBD
### Section 2.4: Dynamic inputs/outputs
TBD
## Chapter 3 : How to create a study in SoSTrades ?
TBD
### Section 3.1 Create your process
TBD
### Section 3.2 Create your usecase or study
TBD
### Section 3.3 Test and validate your study 
TBD
## Chapter 4 : How to create your own repository ? 
1. **Create Repository**
   - Create a new repository on GitHub
   - Follow SoSTrades naming conventions for consistency

2. **Configure Access Management**
   Add the following groups with admin role:
   - Business For Planet Modeling - Devops
   - Business For Planet Modeling - Core developer
   - Business For Planet Modeling - Repository admin

3. **Branch Structure**
   Your repository must include these mandatory branches:
   - `develop`: Main development branch
   - `integration`: Testing branch for deployed integration platform
   - `post_integration`: Pre-validation branch, this platform is used for tests pipeline before merge into validation
   - `validation`:  For validation platform where all tests are validated
   - `main`: Release branch

4. **Development Workflow**
   - Development starts on `develop` branch
   - Then merge the develop into integration
   - Automatic pipeline handles merges through branches
   - Flow: integration → post_integration → validation → main
### Section 4.1: Repository structure
New_repo_name

    new_repo_name
        datasets_database
            datasets
            mappings
        models
            __init__.py
        sos_process
            __init__.py
        tests
            __init__.py
        __init__.py
    .coveragerc
    .gitignore
    LICENSE
    platform_version_required.txt
    pytest
    README.md
    requirements.in

 
### Section 4.2: Connect your repository to your GUI
- If you use the local installation with sostrades-dev-tools:
  1. Locate `sostrades-dev-tools\model_repositories.json`
  2. Add your GitHub repository URL inside this file

