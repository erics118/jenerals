default:
    @just --list --unsorted

# Install dependencies
install:
    pip install -e .

# Run the program
run:
    python3 src/main.py

# Run the program in dev mode, enabling some extra features
dev:
    python3 src/main.py --dev

# Package source code for submission to Autolab
package:
    git ls-files --exclude-standard | zip --names-stdin submissions/`date +%Y-%m-%d-%H.%M.%S`.zip
