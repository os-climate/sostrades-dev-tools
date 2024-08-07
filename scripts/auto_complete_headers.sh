#!/bin/sh

launch_auto_complete() {
   echo $1 Analysing...
   python -m sostrades_core.auto_complete_headers
}

cd ../

cd ./models/sostrades-optimization-plugins
launch_auto_complete sostrades-optimization-plugins

cd -
cd ./models/witness-core
launch_auto_complete witness-core

cd -
cd ./models/witness-energy
launch_auto_complete witness-energy 

cd -
cd ./platform/sostrades-core 
launch_auto_complete sostrades-core 

cd -
cd ./platform/sostrades-ontology 
launch_auto_complete sostrades-ontology 

cd -
cd ./platform/sostrades-webapi 
launch_auto_complete sostrades-webapi 
