from sys import argv


# Override default function
def input(prompt: str = ...) -> str:
	return argv[1]
