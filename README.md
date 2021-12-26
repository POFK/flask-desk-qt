pipenv install -d nuitka
pipenv shell
python -m nuitka --onefile exam.py 
nuitka --onefile --python-flag=no_site --include-data-dir=C:\Users\Tardis\flask-desk-qt\templates=templates --include-data-dir=C:\Users\Tardis\flask-desk-qt\static=static --windows-disable-console --windows-icon-from-ico=opus-logo.ico exam.py