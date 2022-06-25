REM call bumpver update --patch --dry
REM call bumpver update --patch
call bumpver update
del dist\*.* /q
call python -m build
call python -m pip install -e .
REM call twine upload -r testpypi dist/*
call twine upload -r testpypi dist/*