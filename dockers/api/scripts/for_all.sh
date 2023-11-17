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