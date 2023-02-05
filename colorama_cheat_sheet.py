from colorama import Fore, Style, init
init()

fb = f'{Fore.BLACK}'
fblu = f'{Fore.BLUE}'
fc = f'{Fore.CYAN}'
fg = f'{Fore.GREEN}'
fm = f'{Fore.MAGENTA}'
fr = f'{Fore.RED}'
fw = f'{Fore.WHITE}'
fy = f'{Fore.YELLOW}'
flb = f'{Fore.LIGHTBLACK_EX}'
flblu = f'{Fore.LIGHTBLUE_EX}'
flc = f'{Fore.LIGHTCYAN_EX}'
flg = f'{Fore.LIGHTGREEN_EX}'
flm = f'{Fore.LIGHTMAGENTA_EX}'
flr = f'{Fore.LIGHTRED_EX}'
flw = f'{Fore.LIGHTWHITE_EX}'
fly = f'{Fore.LIGHTYELLOW_EX}'

sbb = f'{Style.BRIGHT}{fb}'
sbblu = f'{Style.BRIGHT}{fblu}'
sbc = f'{Style.BRIGHT}{fc}'
sbg = f'{Style.BRIGHT}{fg}'
sbm = f'{Style.BRIGHT}{fm}'
sbr = f'{Style.BRIGHT}{fr}'
sbw = f'{Style.BRIGHT}{fw}'
sby = f'{Style.BRIGHT}{fy}'
sblb = f'{Style.BRIGHT}{flb}'
sblc = f'{Style.BRIGHT}{flc}'
sblg = f'{Style.BRIGHT}{flg}'
sblm = f'{Style.BRIGHT}{flm}'
sblr = f'{Style.BRIGHT}{flr}'
sblw = f'{Style.BRIGHT}{flw}'
sbly = f'{Style.BRIGHT}{fly}'
sbmlblu = f'{Style.BRIGHT}{flblu}'

sdb = f'{Style.DIM}{fb}'
sdblu = f'{Style.DIM}{fblu}'
sdc = f'{Style.DIM}{fc}'
sdg = f'{Style.DIM}{fg}'
sdm = f'{Style.DIM}{fm}'
sdr = f'{Style.DIM}{fr}'
sdw = f'{Style.DIM}{fw}'
sdy = f'{Style.DIM}{fy}'
sdlb = f'{Style.DIM}{flb}'
sdlc = f'{Style.DIM}{flc}'
sdlg = f'{Style.DIM}{flg}'
sdlm = f'{Style.DIM}{flm}'
sdlr = f'{Style.DIM}{flr}'
sdlw = f'{Style.DIM}{flw}'
sdly = f'{Style.DIM}{fly}'
sdmlblu = f'{Style.DIM}{flblu}'

rsr = f'{Fore.RESET}{Style.RESET_ALL}'

colors = [
('fb', f'{Fore.BLACK}'),
('fblu', f'{Fore.BLUE}'),
('fc', f'{Fore.CYAN}'),
('fg', f'{Fore.GREEN}'),
('fm', f'{Fore.MAGENTA}'),
('fr', f'{Fore.RED}'),
('fw', f'{Fore.WHITE}'),
('fy', f'{Fore.YELLOW}'),
('flb', f'{Fore.LIGHTBLACK_EX}'),
('flblu', f'{Fore.LIGHTBLUE_EX}'),
('flc', f'{Fore.LIGHTCYAN_EX}'),
('flg', f'{Fore.LIGHTGREEN_EX}'),
('flm', f'{Fore.LIGHTMAGENTA_EX}'),
('flr', f'{Fore.LIGHTRED_EX}'),
('flw', f'{Fore.LIGHTWHITE_EX}'),
('fly', f'{Fore.LIGHTYELLOW_EX}'),
('sbb', f'{Style.BRIGHT}{fb}'),
('sbblu', f'{Style.BRIGHT}{fblu}'),
('sbc', f'{Style.BRIGHT}{fc}'),
('sbg', f'{Style.BRIGHT}{fg}'),
('sbm', f'{Style.BRIGHT}{fm}'),
('sbr', f'{Style.BRIGHT}{fr}'),
('sbw', f'{Style.BRIGHT}{fw}'),
('sby', f'{Style.BRIGHT}{fy}'),
('sblb', f'{Style.BRIGHT}{flb}'),
('sblc', f'{Style.BRIGHT}{flc}'),
('sblg', f'{Style.BRIGHT}{flg}'),
('sblm', f'{Style.BRIGHT}{flm}'),
('sblr', f'{Style.BRIGHT}{flr}'),
('sblw', f'{Style.BRIGHT}{flw}'),
('sbly', f'{Style.BRIGHT}{fly}'),
('sbmlblu', f'{Style.BRIGHT}{flblu}'),
('sdb', f'{Style.DIM}{fb}'),
('sdblu', f'{Style.DIM}{fblu}'),
('sdc', f'{Style.DIM}{fc}'),
('sdg', f'{Style.DIM}{fg}'),
('sdm', f'{Style.DIM}{fm}'),
('sdr', f'{Style.DIM}{fr}'),
('sdw', f'{Style.DIM}{fw}'),
('sdy', f'{Style.DIM}{fy}'),
('sdlb', f'{Style.DIM}{flb}'),
('sdlc', f'{Style.DIM}{flc}'),
('sdlg', f'{Style.DIM}{flg}'),
('sdlm', f'{Style.DIM}{flm}'),
('sdlr', f'{Style.DIM}{flr}'),
('sdlw', f'{Style.DIM}{flw}'),
('sdly', f'{Style.DIM}{fly}'),
('sdmlblu', f'{Style.DIM}{flblu}')
]

for name, color in colors:
    print(f"{color}This is {name}{rsr}")
