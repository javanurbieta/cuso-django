language: python
dist: xenial
sudo: true

python:
  - 3.10

env:
 global:
  -PIP_VENV_IN_PROJECT=1
  -PIPENV_IGNORE_VIRTUALENVS=1

install:
 -pip install pipenv
 -pipenv sync -d

script:
 - pipenv run flake8
