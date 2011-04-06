You give an image, this slices it into tiles and includes an example page using Google Maps to render it.

slice.py
=======
Splits image file given as command line argument into a set of tiles in 
the static/cart_imgs folder.

Min/max zoom levels and tile width/height are configurable as constants.

The full output path is:

    static/cart_imgs/[zoom]/[x]/[y].png

*Depends on Python Image Magick (tested on Python 2.6+)*

Server
=========
The server.py file is a simple tornado server configured to serve the files
in /static on port 8888.  The example page can be reached at /static/page.html.

*Depends on tornado*

Getting Started
===========

- Get an map image file, run slice (optionally configuring the consts):
    python slice.py [image file]
- Run the dev server, or any other web server rooted at the static/ folder.
- Navigate to the page.html page:
  - With the dev server: localhost:8888/static/page.html
- Cackle with glee.
