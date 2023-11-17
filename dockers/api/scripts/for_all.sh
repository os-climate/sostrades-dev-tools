# Copyright 2023 Capgemini

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Parcourt tous les fichiers et répertoires dans le répertoire courant
for d in *; do
  # Vérifie si l'élément en cours est un répertoire
  if [ -d "$d" ]; then
    # Affiche un message indiquant le répertoire en cours
    echo "Entering directory $d"
    # Change de répertoire dans le sous-répertoire en cours
    cd "$d"
    # Affiche un message indiquant la commande en cours d'exécution
    echo "Running command in directory $d : $*"
    # Exécute la commande donnée en argument
    $*
    # Revient dans le répertoire courant
    cd ..
  fi
done