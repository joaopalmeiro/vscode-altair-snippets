# Development

1. `pipenv install --python 3.8`
2. `pipenv run jupyter lab`
3. `pipenv run python extract_snippet.py`
4. `pipenv run nbqa isort dev.ipynb --nbqa-diff` and `pipenv run nbqa isort dev.ipynb`
5. `pipenv run fmt`

## Notes

- `pipenv run nbqa --help`.
- [mdformat](https://github.com/executablebooks/mdformat):
  - [Plugins](https://mdformat.readthedocs.io/en/stable/users/plugins.html).
  - It can be used with [nbQA](https://github.com/nbQA-dev/nbQA):
    - `pipenv run nbqa mdformat dev.ipynb --nbqa-md --nbqa-diff`.
    - `pipenv run nbqa mdformat dev.ipynb --nbqa-md`.
  - `pipenv install mdformat` or `pipenv install mdformat-gfm`.
  - `pipenv run mdformat .`.
  - `pipenv run mdformat README.md --check`.
  - Useful for applying consecutive numbering to ordered lists created with just `1.`.
