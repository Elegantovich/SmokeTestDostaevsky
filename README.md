# SmokeTestDostaevsky

## Description
Smoke test веб сервиса доставки питания

### Tech
Python 3.11, Selenium 4.13, Pytest 7.4

### How to start a project:
Тестирование производилось на браузере Google chrome. Для старта необходимо узнать версию браузера.
```
chrome://settings/help
```
Clone and move to local repository:
```
git clone https://github.com/Elegantovich/SmokeTestDostaevsky/
```
Load and move in folder 'utilites' driver

Update data/config.ini newest input data

Create a virtual environment (win):
```
python -m venv venv
```
Activate a virtual environment:
```
source venv/Scripts/activate
```
Install dependencies from file requirements.txt:
```
pip install -r requirements.txt
```
Run the script
```
python -m pytest -s -v
```
