import orjson

# Edit before running the script:
NOTEBOOK: str = "dev.ipynb"
ID: str = ""

if __name__ == "__main__":
    with open(NOTEBOOK) as f:
        nb: str = f.read()

    # https://github.com/ijl/orjson#deserialize
    nbo = orjson.loads(nb)

    snippet = nbo["cells"]

    print(snippet)
