Installation process: 
1. create local environment 
```bash
# just on the first time do this
python3 -m venv .venv      # sets up the venv first time

# do this every time before starting the server
source .venv/bin/activate

# OR this if you use fish as a shell
source .venv/bin/activate.fish
```
2. Install required packages
```bash 
pip install -r requirements.txt
```

3. Run the file
```bash
python3 vesting_csv.py
```