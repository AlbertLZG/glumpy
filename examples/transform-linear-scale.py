#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
from glumpy import app
from glumpy.graphics.collections import PointCollection
from glumpy.transforms import LinearScale, Position3D, Viewport

window = app.Window(1024,1024, color=(1,1,1,1))

@window.event
def on_draw(dt):
    window.clear()
    points.draw()

@window.event
def on_mouse_scroll(x,y,dx,dy):

    xdomain, ydomain, zdomain = transform["domain"]
    if dy < 0: ydomain *= 1.1
    else:      ydomain /= 1.1
    transform["domain"] = xdomain, ydomain, zdomain


transform = Position3D(LinearScale()) + Viewport()
points = PointCollection("agg", transform = transform)
points.append( P = np.random.normal(0,.5,(10000,3)) )
app.run()
