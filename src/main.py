# SPDX-License-Identifier: GPL-3.0
# Helix
#
# main.py
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
#
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
import os
import datetime

from lib.icons import icons
from lib.utils import generate_file_links, get_readme_and_format
from lib.globals import root

app = FastAPI()

boot_time = datetime.datetime.now()
version = "0.1.0"
file_listing_html = open("src/html/index.html").read()

@app.get("/css/{file_path:path}")
async def read_css(file_path: str):
    file_path = "src/css/" + file_path
    print(file_path)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.get("/js/{file_path:path}")
async def read_css(file_path: str):
    file_path = "src/js/" + file_path
    print(file_path)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")


@app.get("/", response_class=HTMLResponse)
async def read_root():
    file_links = generate_file_links(root)
    readme = get_readme_and_format(root)
    return file_listing_html.format(
        file_links=file_links, readme=readme, file_path="/", version=version
    )


@app.get("/{file_path:path}")
async def read_file(file_path: str):
    file_path = root + "/" + file_path
    if os.path.isdir(file_path):
        file_links = generate_file_links(file_path)
        readme = get_readme_and_format(file_path)
        return HTMLResponse(
            content=file_listing_html.format(
                file_links=file_links,
                readme=readme,
                file_path=file_path.replace(root, ""),
                version=version,
            )
        )
    elif os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
