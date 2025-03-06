# User Manual

This documentation manual is designed for people seeking to deepen their understanding of using the SoSTrades GUI platform.

SoSTrades is a web-based, multi-user, interactive publication-quality graph simulation platform. It allows users to drop new modules without additional coding, and provides embedded advanced numerical capabilities for simulation and multi-disciplinary optimization. It also has built-in collaborative capabilities to allow different experts to work together.

It provides comprehensive guidance on navigating the GUI for easy interaction. Learn how to create, modify, run, and open userr studies, as well as visualize existing ones.

## Chapter 1: SOSTrades GUI Connexion 

This chapter offers all the necessary explanations for easily connecting the SoSTrades Graphical User Interface. There are possibilities that you can meet to connect on it, the cloud one and the local one.

### Section 1.1: First connexion on cloud landing page

On the cloud login page, a redirection occurs to the Keycloak homepage, allowing authentication with a local Keycloak account created by an administrator. Alternatively, a personal GitHub or Google account can be used by clicking the associated button.

![](images/platform-GUI/login-page/keycloak-login-page.png)


### Section 1.2: Connexion on local machine

The connexion with a developer account is only necessary when user use sostrades in a local environment. A developer account can be created by executing the `CreateUser.py` script of the [SoSTrades local installation documentation](installation.md). The user password can be found in the following path `./sostrades-dev-tools-test-uv/platform/sostrades-webapi/sos_trades_api/secret/`

![](images/platform-GUI/login-page/local-login-page.png)

## Chapter 2: GUI Homepage and Menus

This chapter provides an overview of the GUI homepage, navigation menus, including study and reference management, as well as group management, and finally the Ontology.

### Section 2.1: Homepage infos

![](images/platform-GUI/welcome-page/numbered-welcome-page.png)

After connecting to SoSTrades GUI platform they are many informations displayed on the homepage. Each numbered boxes are describe bellow:
- **1- Menu button:** From this button you can navigate to the different pages of the GUI like return to the homepage, access to study and reference management pages, ontology, group management and manager.
- **2- Platform information:** In this box, the name and creation date of the platform are displayed. When on a hosted platform, the box is clickable to view more details about the different Git repositories the platform is based on.
- **3- User information:** The name of the current user is displayed
- **4- Contact button:** Show the email address of the support team
- **5- Logout button:** Here is the button to logout
- **6- Favorite studies:** At the bottom of the homepage there are the last opened and favorite study of the current user. 
- **7- Header color:** The color of the header is configurable during the platform's creation. For example when the platform is hosted, it has a different color than the purple one used for local platforms.

### Section 2.2: Study Management Visualisation

From the menu button, it is possible to access the study management page and list all the studies that the current user can access, according to their rights on each study, as well as the rights of the groups they belong to. On that page, it is possible to search for a study by its name using the search bar. A study can also be created with the 'Create Study' button, which will be explained in more detail later in this documentation.  
![](images/platform-GUI/header/menu-study.png)
![](images/platform-GUI/study-management/study-management-list.png)

### Section 2.3: Reference management Visualisation

Similar to the study management page, the reference management page can be accessed from the menu button to list references and can also be found using the search bar. A study can be created from a reference, and a reference can be generated.  
![](images/platform-GUI/reference-management/reference-list.png)

### Section 2.4: Group Management
Each user belongs to, at least, one group with rights. 
- **Owner** : When a user create a group, he is the owner of the group. The owner cannot be changed and has the full rights on the group (edition, deletion, manage access rights).
- **Manager** : an edit a group (name and description), manage access rights to the group (can add or remove user or group, but cannot change its own access right nor the owner), can create study into this group. A manager can't delete a group, only the owner can do it.
- **Member** : A member of a group can only create studies into this group. 

These groups contain studies created by user and provide user an access right on it.

When a group is linked to a process, a study, or another group, the users and/or groups within the group inherit the associated access rights.  
For example:  
if a group is added as a manager in a process entity's rights, all users in the group (owner, manager, or member) will be managers of the process.  
If a group is added as a restricted viewer in a study-case entity's rights, all users in the group (owner, manager, or member) will be restricted viewers of the study-case.  
If a user in the restricted viewer group is also added as a manager in the same study-case entity's rights, they will have manager rights for this study-case.

#### Subsection 2.4.1 Create group
![](images/platform-GUI/group-management/create_group.png)  
To create a new group, user must fill in the name and description.  
:warning: Note: If user select confidential, the data will be encrypted. Even developers will not have access to it, and there will be no possibility to directly download the results.

#### Subsection 2.4.2 Select a default group
![](images/platform-GUI/group-management/default_group.png)  
If user select a default group, it will be preselected during a study creation.

#### Subsection 2.4.3 Share a group
If user is manager of the group, he can also add in this group, an other or several users and/or groups, witch can contain several users, by clicking on the share icon ![](images/platform-GUI/icon/icon_share.png)

![](images/platform-GUI/group-management/share_group.png)

This user can also modify the access rights of a user or a group present in this group.  
![](images/platform-GUI/group-management/edit_rights.png)

#### Subsection 2.4.4 Delete a group
![](images/platform-GUI/icon/icon_delete.png)  
**<span style="color: red;">Removing a group will delete all studies that belong to this group.</span>**

### Section 2.5: Ontology Menu

The SoSTrades Ontology is composed of all entities and relationships between concepts used in the Systems of Systems Trades project. The main concepts modeled are Code Repositories, Process Repositories, Processes, Models, Usecases and Parameters. There are represented as OWL Classes and their instances are OWL Individuals. For each instance, the ontology store metadata (label, description, documentation, ...) that are extracted from the Python code stored in the code repositories of the project in Gitlab. This ontology primary purpose is to complement the Web Interface of SoSTrades with these metadata to have a better lisibility and understandability. It is also a good way to explore the available concepts in the SoSTrades platform.

As the same way of other pages of SoSTrades you can access to the Ontology homepage from the menu button at the top left of the homepage and select Ontology.  
![](images/platform-GUI/header/menu-to-ontology-homepage.png)  
In the Ontology homepage, there are four tabs: Homepage, Models, Processes, and Parameters. At the bottom left of the page, a summary list displays the number of code repositories, models, parameters, processes, process repositories, and the usecases. 
![](images/platform-GUI/ontology/ontology-main.png)
By clicking on the Code Repositories link, a table appears displaying information about the different Git repositories used to build the platform.  
![](images/platform-GUI/ontology/ontology-code-traceability.png)  
The three other links, Models, Parameters, and Processes, display the same content as their corresponding tabs at the top of the Ontology homepage.
In the Models tab, a list of all models from each code repository is displayed, including the model name, the number of processes that use the model, and documentation.
![](images/platform-GUI/ontology/ontology-model-list.png)  
With the documentation icon ![](images/platform-GUI/icon/documentation.png) more details about the model can be accessed.  
![](images/platform-GUI/ontology/ontology-model-agri-mix.png)  
In the Processes tab, all processes are listed along with their associated repositories and the number of models used by each process. Additionally, for each process, there are options to create a study from the process, grant access rights to a user or group, and view the process documentation.
![](images/platform-GUI/ontology/ontology-process-list.png)
And lastly, the Parameters tab displays a list of all existing parameters used by a model. More details about each parameter can be accessed using the documentation icon.  
![](images/platform-GUI/ontology/ontology-parameter-list.png)


## Chapter 3: Study Operations
TBD
### Section 3.1: Create a study

 
- ReadOnly mode
- from scratch
- from a reference
- explain all inputs 
- copy a study 

### Section 3.2 Study panels and visualisation
TBD
#### Subsection 3.2.1 Study Panels
Explain treeview, node status, validation state, study link and user collaboration
Explain all study panels (data management, post processing,documentation)
Explain that Dashboard is not implemented yet 
#### Subsection 3.2.2 Study Visualisation
Explain interface diagram, execution sequence & study coupling graph

#### Subsection 3.2.3 Study Logs and notifications
Explain logs & notifications


### Section 3.3 Data management and study configuration
explaon how to save data, how to import data from csv,dataset, ...
### Section 3.4 Study execution

### Section 3.5 Study post-processing
explain post-procs and filters 

### Section 3.6 Open an existing study
explain how to open, edition mode, search variables, filters, fullscreen, user visu (standard, expert)