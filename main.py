"""Entry program for make.fun news-image-20261119 (Python 3.13, stdlib only).

Copies the bundled front-page image to the output directory, deterministically:
the same bytes every run, with no network and no other input.
The image itself is the entry: a 1024x1024 front page for Thursday 19 November 2026.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT, "entry.png"))
