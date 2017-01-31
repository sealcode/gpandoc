#!/bin/sh

############
# Generate *.py files from Qt's *.ui files
############

PYUIC="pyuic5"
CMD=${1:-compile}
UIDIR=ui

cd ui

case "$CMD" in
"compile")
    for f in *.ui
    do
        $PYUIC $f > "`echo $f | cut -d. -f1`.py"
    done
    ;;
"clean")
    rm -f *.py
    ;;
esac
