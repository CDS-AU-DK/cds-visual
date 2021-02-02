#!/usr/bin/env bash

VENVNAME=cv101
jupyter kernelspec uninstall $VENVNAME
rm -r $VENVNAME