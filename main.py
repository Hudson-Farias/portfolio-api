from fastapi import FastAPI

from importlib import import_module
from dotenv import load_dotenv
from os import walk, getenv
from os.path import join

load_dotenv()

DOCS_PATH = getenv("DOCS_PATH")
REDOCS_PATH = getenv("REDOCS_PATH")


app = FastAPI(docs_url = DOCS_PATH, redoc_url = REDOCS_PATH)

def load(subapp: FastAPI, directory: str = "routers"):
    import_cache = {}

    for root, _, files in walk(directory):
        for file in files:
            if not file.startswith("__") and file.endswith(".py"):
                path = join(root, file).replace(".py", "").replace("/", ".").replace("\\", ".")

                if path not in import_cache:
                    import_cache[path] = import_module(path)

                module = import_cache[path]
                subapp.include_router(module.router)

    del import_cache

load(app)
