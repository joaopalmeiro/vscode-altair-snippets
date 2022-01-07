import json

import orjson
import pyperclip

# Edit before running the script:
NOTEBOOK: str = "dev.ipynb"
ID: str = "ab6233dd-0b83-44c8-bf78-a156bf60a5df"


def search_cell(id, notebook):
    # https://stackoverflow.com/a/38865327
    for cell in notebook["cells"]:
        if cell["id"] == id:
            return cell


if __name__ == "__main__":
    with open(NOTEBOOK) as f:
        nb: str = f.read()

    # https://github.com/ijl/orjson#deserialize
    nbo = orjson.loads(nb)

    cell = search_cell(ID, nbo)

    # https://github.com/ijl/orjson#serialize
    snippet = "".join(cell["source"])
    output = json.dumps(f"{snippet}\n", ensure_ascii=False)

    print(output, "Copied to clipboard! 📋", sep="\n" * 2)
    pyperclip.copy(output)
