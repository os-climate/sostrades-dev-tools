#!/bin/sh

# Define your function here
launch_tests() {
   echo $1 testing...
   #test-file-pattern = l1s_test_header.py
   #test-file-pattern = l*_test*.py
   #sed -i -E "s/^test-file-pattern = .{1,}py$/test-file-pattern = l1s_test_header.py/g" nose2.cfg
   #nose2 

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




