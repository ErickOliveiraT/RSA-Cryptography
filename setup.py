from cx_Freeze import setup, Executable
import sys

setup(
    name = "RSA",
    version = "2.0",
    description = "RSA Algorithm",
    executables = [Executable("rsa.py", base = None)])