#!/bin/bash

SESSION_NAME="Sostrades"

# Créer une nouvelle session tmux détachée
tmux new-session -d -s $SESSION_NAME

# Fenêtre principale avec la première commande
tmux send-keys -t $SESSION_NAME "source /sostrades-dev-tools/.venv/bin/activate && cd platform/sostrades-webapi && python3.9 server_scripts/split_mode/launch_server_post_processing.py" C-m

# Créer un nouveau panneau et lancer une autre commande
tmux split-window -v -t $SESSION_NAME
tmux send-keys -t $SESSION_NAME "source /sostrades-dev-tools/.venv/bin/activate && cd platform/sostrades-webapi && python3.9 server_scripts/split_mode/launch_server_main.py" C-m

# Créer un autre panneau horizontalement et lancer une commande
tmux split-window -h -t $SESSION_NAME
tmux send-keys -t $SESSION_NAME "source /sostrades-dev-tools/.venv/bin/activate && cd platform/sostrades-webapi && python3.9 server_scripts/split_mode/launch_server_data.py" C-m

# Créer un autre panneau horizontalement et lancer une commande
tmux split-window -h -t $SESSION_NAME
tmux send-keys -t $SESSION_NAME "source /sostrades-dev-tools/.venv/bin/activate && cd platform/sostrades-webapi && python3.9 server_scripts/split_mode/launch_server_message.py" C-m

# Créer un autre panneau horizontalement et lancer une commande
tmux split-window -h -t $SESSION_NAME
tmux send-keys -t $SESSION_NAME "source /sostrades-dev-tools/.venv/bin/activate && cd platform/sostrades-ontology && python3.9 sos_ontology/rest_api/api.py" C-m

# Créer un autre panneau horizontalement et lancer une commande
tmux split-window -h -t $SESSION_NAME
tmux send-keys -t $SESSION_NAME "source /sostrades-dev-tools/.venv/bin/activate && cd platform/sostrades-webgui &&  nvs use 18.10.0 && export NG_CLI_ANALYTICS='false' && npm start" C-m


# Créer un autre panneau horizontalement et lancer une commande
tmux split-window -h -t $SESSION_NAME
tmux send-keys -t $SESSION_NAME "echo -e 'Below are the tmux commands to control session: \n\n - Navigate between panes using Ctrl-b and arrow keys (Up, Down, Left, Right) \n - Close a single pane by typing exit in it \n - Close the entire session: Ctrl-b : and type kill-session'" C-m




# Ajuster la taille des panneaux pour qu'ils soient égaux
tmux select-layout -t $SESSION_NAME tiled

# Attacher à la session pour observer les commandes
tmux attach -t $SESSION_NAME


# Instructions for user:
# - Navigate between panes using `Ctrl-b` and arrow keys (Up, Down, Left, Right).
# - Close a single pane by typing `exit` in it.
# - Detach from the session without closing it: `Ctrl-b d`.
# - Close the entire session: `Ctrl-b :` and type `kill-session`.