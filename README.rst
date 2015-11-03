Introduction
============

This Plone package adds a viewlet with social buttons.  You can
configure it from the control panel we add.


Usage
-----

- Add this to the eggs of your instance.

- Install in the Add-ons control panel.

- Configure in the Social Footer control panel.


How to add a new provider
-------------------------

For example, add Instagram:

- Add ``instagram`` to the list of ``PROVIDERS`` in
  pareto/socialfooter/browser/interfaces.py.

- Add ``instagram.png`` to the directories in
  ``pareto/socialfooter/browser/mono``::

    circle/black/instagram.png
    circle/white/instagram.png
    rounded/black/instagram.png
    rounded/white/instagram.png
    transparent/black/instagram.png
    transparent/white/instagram.png

- Creating nice icons is left as an exercise for the reader.
