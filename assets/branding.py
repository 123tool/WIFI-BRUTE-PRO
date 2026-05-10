import random

# Colors
R = '\033[31m' # Red
G = '\033[32m' # Green
Y = '\033[33m' # Yellow
B = '\033[34m' # Blue
C = '\033[36m' # Cyan
W = '\033[0m'  # White

def get_banner():
    banners = [
        f"""
{R}  __      __.__ ___________ ____ ___ 
{R} /  \    /  \__|\_   _____/|    |   \
{R} \   \/\/   /  | |    __)  |    |   /
{W}  \        /|  | |     \   |    |  / 
{W}   \__/\  / |__| \___  /   |______/  
{W}        \/           \/              
{Y}     [ Bruteforce Engine v2.0 ]
{C}   Managed by: Spy-E & 123tool{W}
        """
    ]
    return random.choice(banners)

def log_status(msg, type="info"):
    if type == "info":
        print(f"{W}[{B}*{W}] {msg}")
    elif type == "success":
        print(f"{W}[{G}+{W}] {G}{msg}{W}")
    elif type == "error":
        print(f"{W}[{R}!{W}] {R}{msg}{W}")
    elif type == "process":
        print(f"{W}[{Y}>>{W}] {msg}", end="\r")
