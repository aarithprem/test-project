# test-project
brew install pip

Create virtual env and activate
-------------------------------
/usr/bin/python3 -m venv --system-site-packages venv

source venv/bin/activate

pip install selenium

pip install nose

To run tests:
-------------

nosetests -v tests/github_tests.py
