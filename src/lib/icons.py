# SPDX-License-Identifier: GPL-3.0
# Helix
#
# icons.py
# Definitions for icons to use in the file listing
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
#
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

icons = {
    "extentions": [
        [".iso", ".cd", ".dvd"],
        [".tar", ".tar.gz", ".tar.xz", ".tar.bz2"],
        [".img", ".img.gz", ".rom"],
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
		[".deb", ".rpm", ".pkg", ".msi", ".dmg", ".apk"]
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
		"bi bi-box-fill" # packages
    ],
}