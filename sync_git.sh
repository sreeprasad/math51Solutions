#!/bin/bash

rm -rf ./math_51_notes math_51_solution.pdf
cp ~/Downloads/math_51_solution.pdf .
cp ~/Downloads/math_51_notes.zip .
unzip math_51_notes.zip -d math_51_notes
rm math_51_notes.zip
nvim README.md


