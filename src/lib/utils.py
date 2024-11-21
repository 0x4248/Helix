# SPDX-License-Identifier: GPL-3.0
# Helix
#
# utils.py
# General functions for Helix
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
#
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

import os
import markdown
from markdown.extensions.toc import TocExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.meta import MetaExtension

from lib.globals import root
from lib.icons import icons

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
