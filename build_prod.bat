REM call bumpver update --patch --dry
call bumpver update --patch -t final
REM call bumpver update --minor
del dist\*.* /q
call python -m build
call python -m pip install -e .
REM call twine upload -r testpypi dist/*
REM call twine upload -r testpypi dist/*
call twine upload -r pypi dist/*