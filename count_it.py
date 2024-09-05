#! /usr/bin/env python3

from sys import argv

print(*[f"parameters: {len(argv[1:])}", *(f"{arg}: {len(arg)}" for arg in argv[1:])] if len(argv) >= 2 else ["none"], sep='\n')
