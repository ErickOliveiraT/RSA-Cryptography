import sys
from cx_Freeze import setup, Executable

setup(
    name = "RSA",
    version = "1.5",
    description = "RSA Algorithm",
    executables = [Executable("rsa.py", base = None)])