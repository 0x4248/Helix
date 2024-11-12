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
import markdown
from markdown.extensions.toc import TocExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.meta import MetaExtension
import datetime

app = FastAPI()
root = "."
boot_time = datetime.datetime.now()
version = "0.1.0"

file_listing_html = open("src/html/index.html").read()

icons = {
    "extentions": [
        [".iso", ".img", ".img.gz", ".rom"],
        [".tar", ".tar.gz", ".tar.xz", ".tar.bz2"],
        [".img", ".img.gz", ".bin", ".rom"],
        [".pdf"],
        [".txt", ".md", ".rtf", ".doc", ".docx"],
        [
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
            ".svg",
            ".bmp",
            ".webp",
            ".ico",
            ".tiff",
            ".psd",
            ".ai",
            ".eps",
            ".raw",
        ],
        [".bin", ".dump", ".out"],
        [".crt", ".pem", ".key", ".csr", ".crl", ".der"],
        [".tar.gz.enc", ".tar.gz.enc.asc", ".tar.gz.enc.gpg", ".tar.gz.enc.gpg.asc"],
        [".sum", ".sha256", ".sha512", ".md5", ".sha1"],
        [".sig", ".asc", ".gpg", ".sig.asc", ".gpg.asc"],
        [
            ".mov",
            ".mp4",
            ".avi",
            ".mkv",
            ".webm",
            ".flv",
            ".wmv",
            ".mpg",
            ".mpeg",
            ".m4v",
        ],
        [
            ".mp3",
            ".wav",
            ".flac",
            ".ogg",
            ".m4a",
            ".wma",
            ".aac",
            ".aiff",
            ".alac",
            ".ape",
            ".au",
            ".mka",
            ".mid",
            ".midi",
        ],
        [".gz", ".zip", ".rar", ".7z"],
    ],
    "icon": [
        "bi bi-disc-fill",  # iso
        "bi bi-archive",  # zip
        "bi bi-floppy-fill",  # img
        "bi bi-file-pdf",  # pdf
        "bi bi-file-earmark-text",  # txt
        "bi bi-file-image",  # img
        "bi bi-file-earmark-binary",  # bin
        "bi bi-file-lock-fill",  # crt
        "bi bi-file-earmark-lock-fill",  # enc
        "bi bi-file-earmark-check",  # sum
        "bi bi-file-earmark-break",  # sig
        "bi bi-file-play-fill",  # mov
        "bi bi-file-music",  # mp3
        "bi bi-file-zip",  # zip
    ],
}


def generate_file_links(path):
    files = os.listdir(path)
    files.sort(key=lambda x: os.path.isdir(os.path.join(path, x)), reverse=True)
    file_links = ""
    file_links += f'<tr><td><a href="../" class="folder"><i class="bi bi-arrow-left"></i> ..</a></td><td></td></tr>'
    count = 0
    for file in files:
        count += 1
        done_file = False
        classes = ""
        file_path = os.path.join(path, file).replace(root, "")
        if os.path.isdir(os.path.join(path, file)):
            classes = "folder"
            if file.startswith("."):
                classes = "dotfolder"
            file_links += f'<tr><td><a href="{file_path}/" class="{classes}"><i class="bi bi-folder"></i> {file}/</a></td><td>{len(os.listdir(os.path.join(path, file)))} files</td></tr>'
        else:
            if file.split("/")[-1].startswith(".") == True:
                classes = "dotfile"
            for i, ext in enumerate(icons["extentions"]):
                for a in ext:
                    if file.upper().endswith(a.upper()):
                        file_links += f'<tr><td><a href="{file_path}" class="{classes}"><i class="{icons["icon"][i]}"></i> {file}</a></td><td>{os.path.getsize(os.path.join(path, file))} bytes</td></tr>'
                        done_file = True
                        break

            else:
                if not done_file:
                    file_links += f'<tr><td><a href="{file_path}" class="{classes}"><i class="bi bi-file-earmark"></i> {file}</a></td><td>{os.path.getsize(os.path.join(path, file))} bytes</td></tr>'
    if count == 0:
        file_links += f"<tr><td>Empty folder</td><td></td></tr>"
    return file_links


def get_readme_and_format(path):
    readme = ""
    if os.path.isfile(path + "/README.md"):
        with open(path + "/README.md", "r") as f:
            readme = f.read()
            html = "<h2><i class='bi bi-eyeglasses'></i> README.md</h2><hr>"
            html += markdown.markdown(
                readme,
                extensions=[
                    TocExtension(baselevel=2),
                    TableExtension(),
                    FencedCodeExtension(),
                    CodeHiliteExtension(),
                    MetaExtension(),
                ],
            )
            return html
    elif os.path.isfile(path + "/README.txt"):
        with open(path + "/README.txt", "r") as f:
            readme = (
                "<h2><i class='bi bi-eyeglasses'></i> README.txt</h2><hr><pre>"
                + f.read()
                + "</pre>"
            )
            return readme
    elif os.path.isfile(path + "/README"):
        with open(path + "/README", "r") as f:
            readme = (
                "<h2><i class='bi bi-eyeglasses'></i> README</h2><hr><pre>"
                + f.read()
                + "</pre>"
            )
            return readme
    elif os.path.isfile(path + "/README.html"):
        with open(path + "/README.html", "r") as f:
            readme = f.read()
            return readme
    return readme


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
    return file_listing_html.format(file_links=file_links, readme=readme, file_path="/")


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
            )
        )
    elif os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
