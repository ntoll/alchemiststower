The Alchemist's Tower
=====================

This is a point and click adventure story.

My aim was simple: to create an experience reminiscent of the mysterious
explorations found similar games of the past, such as Myst.

It's also an opportunity for me to try to exercise my PyperCard library (a
simple shim around Kivy, that works like HyperCard).

The story starts in a dinghy on Lake Zurich, Switzerland.

Installation
============

Clone the Git repository (apologies that it's so big, I've been using
uncompressed game assets), or download the and unzip the compressed source.

The Alchemist's Tower only works with Python 3. Create a new virtualenv::

    python3 -m venv tower

Then within the root directory of the Git repository install the dependencies::

    pip install -r requirements.txt

Finally, run the game from the root directory of the repository like this::

    python main.py

You should be presented with a screen asking for your name. Please also make
sure you have sound switched on -- it's an important aspect of the game.

I hope you enjoy the game.

Linux Sound Issues
==================

Due to a bug in Kivy, sound may not work on Linux based systems. The fix is
to compile and install the ``ffpyplayer`` package in your virtualenv **before**
installing from ``requirements.txt``.

Links for how to do this can be found at the following GitHub issue:
https://github.com/matham/ffpyplayer/issues/71 (tl;dr - install a bunch of
system wide packages along with your Python headers, then just
``pip install .`` within the virtualenv from the root directory of
the ``ffpyplayer`` Git repository - detailed instructions here:
https://matham.github.io/ffpyplayer/installation.html#linux).

Game Assets
===========

Music - Fratres for Violin by Arvo Pärt (fair use for educational purposes --
this game will be an example for beginners learning to code).

Images - Mostly sourced from Wikicommons and freely licensed photos found on
the internet by folks who'd visited the tower at Bollingen. Edited, re-touched
and photoshopped by the author. All others covered by fair use for educational
purposes -- this game will be an example for beginners learning to code.

SFX - Freesound project.

Font - Free to use Linux Libertine Regular font.
