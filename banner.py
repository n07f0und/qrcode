#!/usr/bin/env python3

import random

banner1 = """
                                            d8b        
                                            88P        
                                           d88         
.d88b,.88P  88bd88b     d8888b d8888b  d888888   d8888b
88P  `88P'  88P'  `    d8P' `Pd8P' ?88d8P' ?88  d8b_,dP
?8b  d88   d88         88b    88b  d8888b  ,88b 88b    
`?888888  d88'         `?888P'`?8888P'`?88P'`88b`?888P'
    `?88                                               
      88b                                              
      ?8P             
"""

banner2 = """
 ▗▄▖ ▗▄▄▖        ▄▄         ▗▖     
 █▀█ ▐▛▀▜▌      █▀▀▌        ▐▌     
▐▌ ▐▌▐▌ ▐▌     ▐▛    ▟█▙  ▟█▟▌ ▟█▙ 
▐▌ ▐▌▐███      ▐▌   ▐▛ ▜▌▐▛ ▜▌▐▙▄▟▌
▐▌ ▐▌▐▌▝█▖     ▐▙   ▐▌ ▐▌▐▌ ▐▌▐▛▀▀▘
 █▄█▘▐▌ ▐▌      █▄▄▌▝█▄█▘▝█▄█▌▝█▄▄▌
 ▝▀█ ▝▘ ▝▀       ▀▀  ▝▀▘  ▝▀▝▘ ▝▀▀ 
   ▝                               
"""
banner3 = """
                    █     
███ ███   ███       █     
█ █ █ █   █   ███ ███ ███ 
█ █ ██    █   █ █ █ █ ███ 
███ █ █   █   █ █ █ █ █   
███ █ █   ███ ███ ███ ███ 
  █                                                            
"""
banner4 = """
  _   _     _   _   _   _  
 / \ / \   / \ / \ / \ / \ 
( Q | R ) ( C | o | d | e )
 \_/ \_/   \_/ \_/ \_/ \_/ 
"""

def banner():
    banners = [banner1, banner2, banner3, banner4]
    return random.choice(banners)