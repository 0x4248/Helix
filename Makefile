# SPDX-License-Identifier: GPL-3.0
# Helix
#
# Makefile
#
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
# 
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.

PYTHON = python3

.PHONY: all

all: run

run:
	$(PYTHON) src/main.py