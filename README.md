# Overleaf link:
https://www.overleaf.com/9648298511mwhpzgdckrky#c7ed45

# How to run the code:
1. Clone the repository
2. Install Conda for Linux (if not already installed):
```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```
```bash
source ~/miniconda3/bin/activate
```
```bash
conda init
```

or for windows in powershell:
```powershell
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda.exe
start /wait "" .\miniconda.exe /S
del miniconda.exe
```
2. Run the following command in Linux Bash or Windows Powershell:
```bash
conda env create -f environment.yaml
conda activate Modern_Physics_project
```
3. Run the python programme:
```bash
python Responsivity_newdata.py
```
