echo "Creating Python virtual environment"
python -m venv .venv

echo "Activating Python virtual environment"
source .venv/bin/activate
source .venv/Scripts/activate

echo "Installing Python dependencies"
pip install -r requirements.txt