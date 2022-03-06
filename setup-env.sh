echo "Creating Python virtual environment"
python3 -m venv .venv

echo "Activating Python virtual environment"
source .venv/bin/activate
# source .venv/Scripts/activate

echo "Installing Python dependencies"
pip3 install -r requirements.txt