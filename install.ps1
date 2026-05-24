# Run this script to set up the environment correctly on Windows + Python 3.11
# Usage: .\install.ps1

python -m pip install --upgrade pip

# Step 1: numpy first and pinned
pip install "numpy>=1.24,<2.0"

# Step 2: verify numpy before continuing
python -c "import numpy; print('numpy OK:', numpy.__version__)"

# Step 3: PyTorch CPU (explicit index required)
pip install torch --index-url https://download.pytorch.org/whl/cpu

# Step 4: everything else (torch already installed, pip will skip it)
pip install -r requirements.txt
