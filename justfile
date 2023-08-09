# List all recipes
default:
    @just --list --unsorted

# Install dependencies
install:
    pip install -e .

# Run the program
run *args:
    python3 src/main.py {{args}}

# Run the program in dev mode, enabling some extra features
dev *args:
    python3 src/main.py --dev {{args}}

# Package source code for submission to Autolab
package:
    git ls-files --exclude-standard | zip --names-stdin submissions/`date +%Y-%m-%d-%H.%M.%S`.zip
