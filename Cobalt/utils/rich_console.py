import subprocess


try:
    from rich.console import Console
    console = Console()
except ModuleNotFoundError as E:
    print("Failed to find rich colour module...")
    req = input("Would you like to try and install it automatically using pip? (y/n)\n>>> ")
    if req.lower() == 'y':
        subprocess.call["pip", "install", "rich"]
        from rich.console import Console
        console = Console()
    else:
        raise E
