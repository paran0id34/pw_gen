import os
import colorama
from itertools import permutations

colorama.init(strip=False)
victim = []
pwd_list = []

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def banner():
    print('{}'.format(colorama.Fore.GREEN))
    print("@@@@@@@   @@@  @@@  @@@                  @@@@@@@@  @@@@@@@@  @@@  @@@")
    print("@@@@@@@@  @@@  @@@  @@@                 @@@@@@@@@  @@@@@@@@  @@@@ @@@")
    print("@@!  @@@  @@!  @@!  @@!                 !@@        @@!       @@!@!@@@")
    print("!@!  @!@  !@!  !@!  !@!                 !@!        !@!       !@!!@!@!")
    print("@!@@!@!   @!!  !!@  @!@                 !@! @!@!@  @!!!:!    @!@ !!@!")
    print("!!@!!!    !@!  !!!  !@!                 !!! !!@!!  !!!!!:    !@!  !!!")
    print("!!:       !!:  !!:  !!:                 :!!   !!:  !!:       !!:  !!!")
    print(":!:       :!:  :!:  :!:                 :!:   !::  :!:       :!:  !:!")
    print(" ::        :::: :: :::   :::::::::::::   ::: ::::   :: ::::   ::   ::")
    print(" :          :: :  : :    :::::::::::::   :: :: :   : :: ::   ::    : ")
    print("")
    print('{}                          by paran0id'.format(colorama.Fore.BLUE))
    print("---------------------------------------------------------------------")
    print('{}'.format(colorama.Fore.CYAN))

def get_info():
    victim.append(input("Имя атакуемого: "))
    victim.append(input("Фамилия атакуемого: "))
    victim.append(input("Его логин: "))
    victim.append(input("Номер телефона жертвы: "))
    victim.append(input("Год рождения: "))
    victim.append(input("Номер месяца (например, январь - 01, декабрь - 12): "))
    victim.append(input("День рождения (например, 01, 02, ..., 12, ...): "))

def generate():
    for i in range(1, len(victim)+1):
        for subset in permutations(victim, i):
            val = ''.join(subset)
            if val not in pwd_list and val != '':
                pwd_list.append(val)
    print('{}Количество сгенерированных паролей: {}'.format(colorama.Fore.GREEN,len(pwd_list)))

def make_dict():
    mydict = "pwd_list.txt"
    if os.path.isfile(mydict):
        print('{}Файл pwd_list.txt уже существует! Выберите один из вариантов:'.format(colorama.Fore.RED))
        print('{}1. Удалить существующий файл и создать новый с таким же именем'.format(colorama.Fore.YELLOW))
        print('{}2. Изменить имя создаваемого словаря'.format(colorama.Fore.YELLOW))
        answer = ''
        while answer != '1' and answer != '2':
            answer = input("Выберите один из предложенных вариантов ответа: ")
        if answer == '1':
            os.remove(mydict)
            write_to_file(mydict)
        if answer == '2':
            mydict = ''
            while len(mydict) == 0:
                mydict = input("Введите новое имя создаваемого словаря: ")
            write_to_file(mydict)
    else:
        write_to_file(mydict)
    print('{}Словарь {} был успешно создан в {}'.format(colorama.Fore.GREEN,mydict,os.path.dirname(os.path.abspath(__file__))))

def write_to_file(filename):
    f = open(filename,'w')
    for pwd in pwd_list:
        f.write(pwd + '\n')
    f.close()

clear_screen()
banner()
get_info()
generate()
make_dict()

