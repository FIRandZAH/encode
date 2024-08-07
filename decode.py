import os, sys
try:
    __import__("decode").main()
except Exception as e:
    exit(str(e))
