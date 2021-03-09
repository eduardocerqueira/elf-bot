## install

pre-requisites:
* python3
* git

clone elf project to your local machine:

```
git clone git@github.com:eduardocerqueira/elf-bot.git
```

prepare python virtual environment:

```
cd elf-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

running tests:

```
pytest -v tests/test_commands.py
or
pytest -svx tests/test_giphy.py -k test_populate_list
```
