Project 2 CS 4732 SS2023 Terry Ford Jr.
Sources: https://www.youtube.com/watch?v=gyPuAJfOnGk&t=452s

I attempted to use python in vim on delmar and got a warning for using sudo unauthorized
https://xkcd.com/838/

I chose to go with Python in vscode and installed these packages from .vscode terminal
pip install cryptography
pip install pylance
pip install pycryptodome  
I had a lot of issues with pip install pycrypto but I think pycryptodome is a superset
of pycrypto. pycryptodome is the only package I actually used for the project, I believe.

get_random_bytes(32) was used to generate key
from Crypto.Random import get_random_bytes from pip install pycryptodome

