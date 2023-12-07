#!/bin/bash

# Create root directory structure
mkdir -p Frontend/src Frontend/assets Frontend/components Frontend/navigation Frontend/screens Frontend/utils
mkdir -p Backend/api Backend/models Backend/services Backend/tests Backend/utils Backend/config
mkdir -p Database
mkdir -p Scripts
mkdir -p Docs
touch README.md LICENSE .gitignore docker-compose.yml requirements.txt package.json setup.py

# Initialize Git
git init

# Create .gitignore content
cat > .gitignore <<EOF
# Node
node_modules/

# Python
*.pyc
__pycache__/
venv/

# IDEs
.idea/
.vscode/

# OS files
.DS_Store

# Logs
*.log

# Secrets
/secrets/
EOF

echo "Repository setup complete."
