echo off

IF %1.==. GOTO end
IF %1==virtualenv GOTO virtualenv
IF %1==install GOTO install
IF %1==test GOTO test
IF %1==fmt GOTO fmt
IF %1==lint GOTO lint
IF %1==clean GOTO clean
IF %1==venv_off GOTO venv_off

:virtualenv
  ECHO virtualenv
  python -m venv .venv --clear
  .\.venv\Scripts\activate.bat
GOTO end

:install
  ECHO install
  .\.venv\Scripts\pip install --user --upgrade pip
  .\.venv\Scripts\pip install -e .[test]
GOTO end

:test
  ECHO test
  pytest -v --cov-config .coveragerc --cov=test_framework -l --tb=short --maxfail=1 tests/
  coverage xml
  coverage html
GOTO end

:fmt
  ECHO fmt
  isort test_framework/
  black -l 79 test_framework/
  black -l 79 tests/
GOTO end

:lint
  ECHO lint
  flake8 test_framework/
  black -l 79 --check test_framework/
  black -l 79 --check tests/
  mypy --ignore-missing-imports test_framework/
GOTO end

:clean
  ECHO clean
  @REM   dir *.pyc /b/s
  FOR /d /r . %%d IN (__pycache__) DO @IF EXIST "%%d" rd /s /q "%%d"
  FOR /d /r . %%d IN (.pytest_cache) DO @IF EXIST "%%d" rd /s /q "%%d"
  FOR /d /r . %%d IN (.cache) DO @IF EXIST "%%d" rd /s /q "%%d"
  FOR /d /r . %%d IN (.mypy_cache) DO @IF EXIST "%%d" rd /s /q "%%d"
  FOR /d /r . %%d IN (build) DO @IF EXIST "%%d" rd /s /q "%%d"
  FOR /d /r . %%d IN (dist) DO @IF EXIST "%%d" rd /s /q "%%d"
  FOR /d /r . %%d IN (*.egg-info) DO @IF EXIST "%%d" rd /s /q "%%d"
  FOR /d /r . %%d IN (htmlcov) DO @IF EXIST "%%d" rd /s /q "%%d"
  FOR /d /r . %%d IN (.tox/) DO @IF EXIST "%%d" rd /s /q "%%d"
GOTO end

:venv_off
  ECHO venv_off
  .\.venv\Scripts\deactivate.bat
GOTO end

:end
    echo end make
