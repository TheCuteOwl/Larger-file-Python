
import random, string
import shutil
from pathlib import Path
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style

Debug = input(Fore.BLUE + '''Do you want enable debug mode?

[1] = True
[2] = False

->        ''')

if Debug == 1:
    print(Fore.BLUE + 'Now the script will print every action')
else:
    print(Fore.BLUE + 'Some action will be printed')


src_file = input('Drag an Python File -> ')
a = Path(src_file).stem
dest_file = f'{a} New.py'
shutil.copy(src_file, dest_file)

lining = 1
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

Choice = input('''How much do you want the file to grow?

[1] = ~ 5x Bigger
[2] = ~ 45 
[3] = ~ 500 (Take more time)
[4] = ~ 5000 (NEED TO WAIT A LOT (Minutes))

->            ''')

if Choice == '1':
    print('\nWait...')
    f= open(f'{a} temp.py',"w+")
    new = f'{a} temp.py'
    with open(f'{src_file}', 'r') as input_file:
        with open(new, 'w') as output_file:
            for line in input_file:
                line = line.rstrip('\n')
                line = line + f"# {random_char(125)}\n"
                output_file.write(line)
                
                if Debug == '1':
                    print(str(f"{lining} line done"))
                    lining += 1
                else:
                    pass
    input('Finish, press enter to leave')

elif Choice == '2':
    print('\nWait...')
    f= open(f'{a} temp.py',"w+")
    new = f'{a} temp.py'
    with open(f'{src_file}', 'r') as input_file:
        with open(new, 'w') as output_file:
            for line in input_file:
                line = line.rstrip('\n')
                line = line + f"# {random_char(1500)}\n"
                output_file.write(line)
                
                if Debug == '1':
                    print(str(f"{lining} line done"))
                    lining += 1
                else:
                    pass
    input('Finish, press enter to leave')

elif Choice == '3':
    print('\nWait...')
    f= open(f'{a} temp.py',"w+")
    new = f'{a} temp.py'
    with open(f'{src_file}', 'r') as input_file:
        with open(new, 'w') as output_file:
            for line in input_file:
                line = line.rstrip('\n')
                line = line + f"# {random_char(15000)}\n"
                output_file.write(line)
                
                if Debug == '1':
                    print(str(f"{lining} line done"))
                    lining += 1
                else:
                    pass
    input('Finish, press enter to leave')

elif Choice == '4':
    print('\nWait...')
    f= open(f'{a} temp.py',"w+")
    new = f'{a} temp.py'
    with open(f'{src_file}', 'r') as input_file:
        with open(new, 'w') as output_file:
            for line in input_file:
                line = line.rstrip('\n')
                line = line + f"# {random_char(150000)}\n"
                output_file.write(line)
                
                if Debug == '1':
                    print(str(f"{lining} line done"))
                    lining += 1
                else:
                    pass
    input('Finish, press enter to leave')


else:input('Wrong input, press any key to quit')
