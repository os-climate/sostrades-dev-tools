#!/bin/sh

# Define your function here
launch_tests() {
   echo $1 testing...
   pytest -v ./$2/tests/l1s_test_header.py::Testheader
}

cd ./models/witness-core
launch_tests witness-core climateeconomics

cd -
cd ./models/witness-energy
launch_tests witness-energy energy_models

cd -
cd ./platform/sostrades-core 
launch_tests sostrades-core sostrades_core

cd -
cd ./platform/sostrades-ontology 
launch_tests sostrades-ontology sos_ontology

cd -
cd ./platform/sostrades-webapi 
launch_tests sostrades-webapi sos_trades_api




