import os
from pystyle import Center, Colorate, Colors

def ascii_art():
    art = """
    ___                   ___     
   /   | ____________  __/ (_)____
  / /| |/ ___/ ___/ / / / / / ___/
 / ___ / /__/ /  / /_/ / / / /__  
/_/  |_\\___/_/   \\__, /_/_/\\___/  
                /____/               

❱ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ /ᴊᴡᴇ0                                    
"""
    print(Colorate.Color(Colors.cyan , art))

def clear_screen():
    os.system("clear")