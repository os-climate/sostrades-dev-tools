#!/bin/sh

# Define your function here
launch_tests() {
   echo $1 testing...
   #test-file-pattern = l1s_test_header.py
   #test-file-pattern = l*_test*.py
   sed -i -E "s/^test-file-pattern = .{1,}py$/test-file-pattern = l1s_test_header.py/g" nose2.cfg

   nose2 
}

cd ./models/witness-core
launch_tests witness-core

cd -
cd ./models/witness-energy
launch_tests witness-energy

cd -
cd ./platform/sostrades-core
launch_tests sostrades-core

cd -
cd ./platform/sostrades-ontology
launch_tests sostrades-ontology

cd -
cd ./platform/sostrades-webapi
launch_tests sostrades-webapi




