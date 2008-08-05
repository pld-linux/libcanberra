#!/bin/sh

if [ -z "$GTK_MODULES" ] ; then
        GTK_MODULES="libcanberra-gtk-module.so"
else
        GTK_MODULES="$GTK_MODULES:libcanberra-gtk-module.so"
fi

export GTK_MODULES
