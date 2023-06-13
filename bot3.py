from math import pi, sin, cos
from colorama import Fore, Style
import random
import datetime
import re

class Bot:
    def __init__(self):
        self.magenta = Fore.MAGENTA + Style.NORMAL
        self.cyan = Fore.CYAN + Style.BRIGHT
        self.responses = { 'вставочки': [f'{self.magenta}Погоджуюсь, цікава тема! \U0001F601 ', f'{self.magenta}Чудовий вибір! \U0001F609 ',
                                     f'{self.magenta}Cкладна тема, але будемо  розбиратись! \U0001F605 ', f'{self.magenta}Неочікуваний вибір! \U0001F609 '], 
                        'ерор': [f'{self.magenta}Не знаю такої команди \U0001F641 ', f'{self.magenta}Помилка! Спробуйте ввести ще раз \U0001FAE1 ', 
                                 f'{self.magenta}Схоже, що щось не так. Перечитай інструкції і спробуй ввести ще раз \U0001F642 '	],
                        'гудбай': [f'{self.magenta}Класно поспілкувались, залітай ще! \U0001F970 ', f'{self.magenta}Бувай! \U0001F929 ', f'{self.magenta}Сумуватиму за тобою! \U0001F972 ']}
        self.dialog = []  
    
    def greet(self):
        message = 'Привіт, я бот Володька \U0001F607. '
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')
     
    def select_topic(self):
        while True:
            message = f'\nЯ можу відповідати на питання з таких тем: математика, фізика, філологія, географія, робота з текстом, загальне та декілька інших завдань, \nщоб дізнатися їх, наберіть "інше". Для завершення розмови надрукуйте "вихід". Що обираємо? '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}', end='')
            topic = input(self.cyan).lower().strip(' .123456789/@#$%^&*()_+=')
            self.dialog.append(('User', topic, datetime.datetime.now().strftime('%H:%M:%S')))

            if topic[:3] == 'мат':
                self.select_math_problem()

            elif topic[:3] == 'фіз':
                self.physics_problem()

            elif topic[:3] == 'гео':
                self.select_geography_problem()

            elif topic[:3] == 'філ':
                self.select_philology_problem()

            elif topic == 'робота з текстом':
                self.text_handling()

            elif topic == 'загальне':
                self.common()

            elif topic == 'інше':
                self.others()

            elif topic == 'вихід':
                message = random.choice(self.responses['гудбай'])
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message)
                break

            else:
                message = random.choice(self.responses['ерор'])
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message)
                continue

    def select_math_problem(self):
        message = random.choice(self.responses['вставочки'])
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(message)
        while True:
            message = '''\nОбрано розділ "математика". Оберіть задачу з перерахованих (можете написати її номер, повністю задачу або ключове слово), 
якщо бажаєте повернутись до головного меню, введіть "назад":
        1. Знаходження векторного добутку векторів
        2. Обчислення відстані від точки до прямої в просторі
        3. Знайти площу кола
        4. Вивести sin(x) та cos(x): '''
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}')
            subtopic = input(self.cyan).lower().strip('./@#$%^&*()_+=')
            self.dialog.append(('User', subtopic, datetime.datetime.now().strftime('%H:%M:%S')))

            if subtopic in ['1', 'добуток', 'знаходження', 'векторний добуток векторів', 'знаходження векторного добутку векторів']:
                self.calculate_vector_product()

            elif subtopic in ['2', 'відстань', 'точка', 'пряма', 'обчислення відстані від точки до прямої в просторі']:
                self.calculate_distance_to_line()

            elif subtopic in ['3', 'площа', 'коло', 'знайти площу кола']:
                self.calculate_square()

            elif subtopic in ['4', 'властивості', 'синус', 'вивести sin(x) та cos(x)']:
                self.sin_cos()

            elif subtopic == 'назад':
                break

            else:
                message = random.choice(self.responses['ерор'])
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message)
                continue

    def calculate_vector_product(self):
        numbers = []
        message = f'''{random.choice(self.responses['вставочки'])}Якщо бажаєте повернутись до попереднього меню, введіть "назад"'''
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')
        message = f'{Style.BRIGHT}\nЗВЕРНІТЬ УВАГУ, {self.magenta}що якщо бажаєте ввести дробне число, вводьте його через крапку, наприклад 4.25 '
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(message)
        for i in range(3):
            while True:
                message = f'{self.magenta}Введіть координату номер {i+1} {Style.BRIGHT}першого {self.magenta}тривимірного вектора: {self.cyan}'
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message, end='')
                coord = input(self.cyan).lower()
                self.dialog.append(('User', coord, datetime.datetime.now().strftime('%H:%M:%S')))
                if coord == 'назад':
                    return
                try:
                    coord = float(coord)
                    break
                except:
                    message = random.choice(self.responses['ерор'])
                    self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                    print(message)
                    continue
            numbers.append(coord)
            i += 1
        print()
        for i in range(3):
            while True:
                message = f'{self.magenta}Введіть координату номер {i+1} {Style.BRIGHT}другого {self.magenta}тривимірного вектора: {self.cyan}'
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message, end='')
                coord = input(self.cyan).lower()
                self.dialog.append(('User', coord, datetime.datetime.now().strftime('%H:%M:%S')))
                if coord == 'назад':
                    return
                try:
                    coord = float(coord)
                    break
                except:
                   message = random.choice(self.responses['eror'])
                   self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                   print(message)
                   continue
            numbers.append(coord)
            i += 1

        first = round((numbers[1] * numbers[5]) - (numbers[2] * numbers[4]), 2)
        second = round((numbers[2] * numbers[3]) - (numbers[0] * numbers[5]), 2)
        third = round((numbers[0] * numbers[4]) - (numbers[1] * numbers[3]), 2)

        message = f'Векторний добуток векторів А{numbers[0], numbers[1], numbers[2]} і  В{numbers[3], numbers[4], numbers[5]} дорівнює C{first, second, third}'
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

    def calculate_square(self):
        message1 = f'''{random.choice(self.responses['вставочки'])}Якщо бажаєте повернутись до попереднього меню, введіть "назад"'''
        self.dialog.append(('Bot', message1, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message1}')
        message2 = f'{Style.BRIGHT}\nЗВЕРНІТЬ УВАГУ, {self.magenta}що якщо бажаєте ввести дробне число, вводьте його через крапку, наприклад 4.25 '
        self.dialog.append(('Bot', message2, datetime.datetime.now().strftime('%H:%M:%S')))
        print(message2)
        return_to_menu = False
        while not return_to_menu:
            message = 'Введіть радіус кола: '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}', end='')
            radius = input(self.cyan).lower()
            self.dialog.append(('User', radius, datetime.datetime.now().strftime('%H:%M:%S')))
            try:
                radius = float(radius)
                S, s = float(radius)**2, float(radius)**2*pi
                message = f'Площа кола з радіусом {radius} см дорівнює {S}π см² або {round(s, 3)} см²'
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(f'{self.magenta}{message}')
                return_to_menu = True
            except:
                if radius == 'назад':
                    return_to_menu = True
                else:
                    message = random.choice(self.responses['ерор'])
                    self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                    print(message)

    def calculate_distance_to_line(self):
        message1 = f'''{random.choice(self.responses['вставочки'])}Якщо бажаєте повернутись до попереднього меню, введіть "назад"'''
        self.dialog.append(('Bot', message1, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message1}')
        message2 = f'{Style.BRIGHT}\nЗВЕРНІТЬ УВАГУ, {self.magenta}що якщо бажаєте ввести дробне число, вводьте його через крапку, наприклад 4.25 '
        self.dialog.append(('Bot', message2, datetime.datetime.now().strftime('%H:%M:%S')))
        print(message2)
        coordinates = []
        for i in range(3):
            while True:
                message = f'{self.magenta}Введіть координату номер {i+1} {Style.BRIGHT}точки Р: '
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message, end='')
                coord = input(self.cyan).lower()
                self.dialog.append(('User', coord, datetime.datetime.now().strftime('%H:%M:%S')))
                if coord == 'назад':
                    return
                try:
                    coord = float(coord)
                    break
                except:
                    message = random.choice(self.responses['ерор'])
                    self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                    print(message)
                    continue
            coordinates.append(coord)
            i += 1
        print()
        for i in range(3):
            while True:
                message = f'{self.magenta}Введіть координату номер {i+1} {Style.BRIGHT}точки А на прямій: {self.cyan}'
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message, end='')
                coord = input(self.cyan).lower()
                self.dialog.append(('User', coord, datetime.datetime.now().strftime('%H:%M:%S')))
                if coord == 'назад':
                    return
                try:
                    coord = float(coord)
                    break
                except:
                    message = random.choice(self.responses['ерор'])
                    self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                    print(message)
                    continue
            coordinates.append(coord)
            i += 1
        print()
        for i in range(3):
            while True:
                message = f'{self.magenta}Введіть координату номер {i+1} {Style.BRIGHT}точки В на прямій: {self.cyan}'
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message, end='')
                coord = input(self.cyan).lower()
                self.dialog.append(('User', coord, datetime.datetime.now().strftime('%H:%M:%S')))
                if coord == 'назад':
                    return
                try:
                    coord = float(coord)
                    break
                except:
                    message = random.choice(self.responses['ерор'])
                    self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                    print(message)
                    continue
            coordinates.append(coord)
            i += 1

        p_a = [coordinates[0] - coordinates[3], coordinates[1] - coordinates[4], coordinates[2] - coordinates[5]]
        p_b = [coordinates[0] - coordinates[6], coordinates[1] - coordinates[7], coordinates[2] - coordinates[8]]
        b_a = [coordinates[6] - coordinates[3], coordinates[7] - coordinates[4], coordinates[8] - coordinates[5]]

        cross_product = [
        p_a[1] * p_b[2] - p_a[2] * p_b[1],
        p_a[2] * p_b[0] - p_a[0] * p_b[2],
        p_a[0] * p_b[1] - p_a[1] * p_b[0]
    ]
        cross_product_length = (cross_product[0] ** 2 + cross_product[1] ** 2 + cross_product[2] ** 2) ** 0.5
        b_a_length = (b_a[0] ** 2 + b_a[1] ** 2 + b_a[2] ** 2) ** 0.5

        distance = cross_product_length / b_a_length

        message = f'Відстань від точки P{coordinates[0], coordinates[1], coordinates[2]} до прямої AB{coordinates[3:6]}, {coordinates[6:9]} дорівнює {distance}'
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

    def sin_cos(self):
        message1 = f"{random.choice(self.responses['вставочки'])}"
        self.dialog.append(('Bot', message1, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message1}')
        while True:
            message2 = f'{Style.BRIGHT}\nЗВЕРНІТЬ УВАГУ, {self.magenta}що якщо бажаєте ввести дробне число, вводьте його через крапку, наприклад 4.25 '
            self.dialog.append(('Bot', message2, datetime.datetime.now().strftime('%H:%M:%S')))
            print(message2)
            message = '''Уведіть число, синус та косинус якого ви хочете порахувати; 
якщо бажаєте повернутись до попереднього меню, введіть "назад": '''
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}', end='')
            num = input(self.cyan).lower().strip('/@#$%^&*()_+=')
            self.dialog.append(('User', num, datetime.datetime.now().strftime('%H:%M:%S')))
            if num == 'назад':
                return
            try:
                num = float(num)
                ssin, ccos = sin(num), cos(num)
                message = f'sin({num}) = {round(ssin, 3)}, cos({num}) = {round(ccos, 3)}.'
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(f'{self.magenta}{message}')
                break
            except:
                message = random.choice(self.responses['ерор'])
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message)
                continue
    
    def physics_problem(self):
        while True:
            message = f'\nРозділ "фізика" має тільки одну тему: "Порахувати силу взаємодії двох точкових зарядів за законом Кулона". \nЯкщо бажаєте продовжити, введіть "так", якщо ні -"ні" або "назад", тоді ви повернетесь у попереднє меню: '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}', end='')
            yes_or_no = input(self.cyan).lower().strip('.123456789/@#$%^&*()_+=')
            self.dialog.append(('User', yes_or_no, datetime.datetime.now().strftime('%H:%M:%S')))
            if yes_or_no == 'так': break
            elif yes_or_no in ('ні', 'назад'): return
            else:
                message = random.choice(self.responses['ерор'])
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message)
                continue
        message = random.choice(self.responses["вставочки"])
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

        while True:
            message2 = f'{Style.BRIGHT}\nЗВЕРНІТЬ УВАГУ, {self.magenta}що якщо бажаєте ввести дробне число, вводьте його через крапку, наприклад 4.25 '
            self.dialog.append(('Bot', message2, datetime.datetime.now().strftime('%H:%M:%S')))
            print(message2)
            message = f'{self.magenta}Уведіть заряд {Style.BRIGHT}першого {self.magenta}об\'єкта, або введіть "назад" для повернення до вибору розділів: '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(message, end='')
            q1 = input(self.cyan).lower()
            self.dialog.append(('User', q1, datetime.datetime.now().strftime('%H:%M:%S')))
            message = f'{self.magenta}Уведіть заряд {Style.BRIGHT}другого {self.magenta}об\'єкта, або введіть "назад" для повернення до вибору розділів: '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(message, end='')
            q2 = input(self.cyan).lower()
            self.dialog.append(('User', q2, datetime.datetime.now().strftime('%H:%M:%S')))
            message = f'Уведіть відстань між об\'єктами, або введіть "назад" для повернення до вибору розділів: '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}', end='')
            r = input(self.cyan).lower()
            self.dialog.append(('User', r, datetime.datetime.now().strftime('%H:%M:%S')))
            
            if q1 == 'назад' or q2 == 'назад' or r == 'назад': return    
            try:
                q1 = float(q1)
                q2 = float(q2)
                r = float(r)
                k = 9
                Force = k * abs(q1) * abs(q2) / (r ** 2)
                message = f'Формула закону Кулона виглядає так: F = k*(|q1|*|q2|)/r², підставляємо значення у неї: F = 9 * 10^(9) * ( |{q1}| * |{q2}| ) / {r}² = {round(Force, 2)} * 10^(9)  .'
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(f'{self.magenta}{message}')
                break
            except:
                message = f'\nСхоже, що не всі введені вами значення підходять, має бути три числа, перевірте і спробуйте ввести ще раз \U0001F642 '
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(f'{self.magenta}{message}')

    def select_geography_problem(self):
        message = random.choice(self.responses['вставочки'])
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(message)
        while True:
            message = '''\nОбрано розділ "географія". Оберіть задачу з перерахованих (напишіть її номер), 
якщо бажаєте повернутись до головного меню, введіть "назад":
        1. 5 найвищих гір у світі та їхні висоти.
        2. Який материк найбільший за площею?
        3. Найбільші водосховища світу : '''
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}')
            subtopic = input(self.cyan).lower().strip('./@#$%^&*()_+=')
            self.dialog.append(('User', subtopic, datetime.datetime.now().strftime('%H:%M:%S')))

            if subtopic == '1':
                self.mountaints()

            elif subtopic == '2':
                self.mainland()

            elif subtopic == '3':
                self.reservoirs()

            elif subtopic == 'назад':
                break

            else:
                message = random.choice(self.responses['ерор'])
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message)
                continue

    def mountaints(self):
        message = f'''\nТоп-5 найвищих гір у світі:
        1. Еверест - 8848 м
        2. Аконкагуа - 6962 м
        3. Деналі - 6191 м
        4. Кіліманджаро - 5895 м 
        5. Крістобаль-Колон - 5700 м. '''
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

    def mainland(self):
        message = f'''\nЄвразія — найбільший материк на Землі, що складається з Європи та Азії. Розташований в основному між північною та східною півкулями, \nмежує з Атлантичним океаном на заході, Тихим на сході, Північно-Льодовитим на півночі, а також Африкою, Середземним морем та Індійським океаном на півдні. '''
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

    def reservoirs(self):
        message = f'''\nНайбільші за площею водосховища світу:
        1. Озеро Вольта (8482 км²; Гана)
        2. Смолвуд (6527 км²; Канада)
        3. Куйбишевське водосховище (6450 км²; Росія)
        4. Озеро Кариба (5580 км²; Зімбабве, Замбія)
        5. Бухтарминське водосховище (5490 км²; Казахстан)
        6. Братське водосховище (5426 км²; Росія)
        7. Озеро Насера (5248 км²; Єгипет, Судан)
        8. Рибінське водосховище (4580 км²; Росія) '''
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')
    
    def select_philology_problem(self):
        message = random.choice(self.responses['вставочки'])
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(message)
        while True:
            message = '''\nОбрано розділ "філологія". Оберіть задачу з перерахованих (напишіть її номер), 
якщо бажаєте повернутись до головного меню, введіть "назад":
        1. Яка різниця між іменником та прикметником?
        2. Як утворити форму множини іменників в українській мові? : '''
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}')
            subtopic = input(self.cyan).lower().strip('./@#$%^&*()_+=')
            self.dialog.append(('User', subtopic, datetime.datetime.now().strftime('%H:%M:%S')))

            if subtopic == '1':
                self.adjectives()

            elif subtopic == '2':
                self.nouns()

            elif subtopic == 'назад':
                break

            else:
                message = random.choice(self.responses['ерор'])
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message)
                continue

    def adjectives(self):
        message = f'''\nІменник і прикметник - самостійні частини мови, проте в реченні між ними завжди встановлюється зв'язок, \nпри якому іменник виступає в ролі домінанти, а прикметник - в ролі залежного слова. 
Іменник - частина мови, яка називає предмет, явище або стан і відповідає на питання хто? або що?
Кожен предмет або явище має певні ознаки, що конкретизують його значення. Слова, які називають ознаку предмета, є прикметниками. \nВони відповідають на питання який? яка? яке? в залежності від роду іменника, до якого відносяться. \nНаприклад, зелене яблуко - "зелене" - ознака, прикметник; "яблуко" - предмет, іменник.'''
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

    def nouns(self):
        message = '''
    - іменники середнього роду мають у називному і знахідному відмінках однини закінчення -а або -я (-й-а). Наприклад, озеро-озера, море-моря;
    - іменники чоловічого роду 2-ї відміни із закінченням -ин утворюють множину заміною його на -и (боярин — бояри, громадянин — громадяни);
    - іменники дитина і людина утворюють множину заміною закінчення -ина на -и, у слові дитина також змінюється голосний кореня (діти, люди);
    - іменники IV-ї відміни утворюють множину за допомогою суфіксів-нарощень -ен, -ат (імена, племена, ягнята); 
    - іменники ІІ-ї відміни небо і чудо — за допомогою нарощення суфікса -ес (небеса, чудеса); 
    - за допомогою нарощення утворювали колись множину й такі слова, як слово, коло, тіло. Надалі всі слова з основою на *-s стали змінюватися 
    за відмінками і числами аналогічно іменникам середнього роду з основою на *-o, від цього способу утворення множини залишилися такі релікти, 
    як форми множини небеса, чудеса, а також прикметники тілесний і словесний (від тілеса і словеса). Іменник коло теж став утворювати множину 
    за зразком слів на *-o (кола), але часто вживана стара форма множини колеса, зробивши нарощення -ес частиною кореня, «переосмислила» цю 
    форму як множину від нового слова колесо. '''
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

    def text_handling(self):
        message = random.choice(self.responses['вставочки'])
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(message)
        while True:
            message = '''\nОбрано розділ "робота з текстом". Оберіть задачу з перерахованих (напишіть її номер), 
якщо бажаєте повернутись до головного меню, введіть "назад":
        1. Вивести список всіх унікальних слів у тексті
        2. Вивести вміст файлу в зворотному порядку
        3. Перевести текст в нижній регістр.  : '''
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}')
            subtopic = input(self.cyan).lower().strip('./@#$%^&*()_+=')
            self.dialog.append(('User', subtopic, datetime.datetime.now().strftime('%H:%M:%S')))

            if subtopic == '1':
                self.get_unique_words()

            elif subtopic == '2':
                self.reversed_file()

            elif subtopic == '3':
                self.lowercase()

            elif subtopic == 'назад':
                break

            else:
                message = random.choice(self.responses['ерор'])
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message)
                continue

    def get_unique_words(self):
        self.words = []
        while True:
            message = f'Введіть шлях до файла, з яким необхідно працювати у вигляді D:\myfiles\welcome.txt, \nякщо бажаєте повернутись назад, введіть "назад": '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}', end = '')
            input_file = input(self.cyan)
            self.dialog.append(('User', input_file, datetime.datetime.now().strftime('%H:%M:%S')))
            if input_file == 'назад': return
            try:
                with open(input_file, 'r', encoding='utf-8') as file:
                    text = file.read()
                    break
            except FileNotFoundError:
                message = f"Файл '{input_file}' не знайдено, спробуйте ввести ще раз."
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(f'{self.magenta}{message}')
                continue
        # Розділити текст на окремі слова
        text = text.lower()
        words = text.split()
        # Видалити розділові знаки
        words = [word.strip('/,.!?:;()"«»\'[]1234567890\\') for word in words]
        # Додати унікальні слова до списку
        self.words.extend(set(words))
        print()
        while True:
            message = f'Введіть шлях до файла, до якого записувати результат у вигляді D:\myfiles\welcome.txt, \nякщо бажаєте повернутись назад, введіть "назад": '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}', end = '')
            output_file = input(self.cyan)
            self.dialog.append(('User', output_file, datetime.datetime.now().strftime('%H:%M:%S')))
            if output_file == 'назад': return
            try:
                with open(output_file, 'w', encoding='utf-8') as file:
                    for word in self.words:
                        file.write(word + '\n')
                    break
            except:
                message = f"Не вдалося записати до файлу '{output_file}', спробуйте ввести ще раз."
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(f'{self.magenta}{message}')
                continue
        message =f"""\nСписок унікальних слів з файлу {input_file} наведено нижче, також його збережено до файлу {output_file}: 
{self.words}"""
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

    def reversed_file(self):
        while True:
            message = f'Введіть шлях до файла, з яким необхідно працювати у вигляді D:\myfiles\welcome.txt, \nякщо бажаєте повернутись назад, введіть "назад": '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}', end = '')
            input_file = input(self.cyan)
            self.dialog.append(('User', input_file, datetime.datetime.now().strftime('%H:%M:%S')))
            if input_file == 'назад': return
            try:
                with open(input_file, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    reversed_lines = reversed(lines)
                    break
            except FileNotFoundError:
                message = f"Файл '{input_file}' не знайдено, спробуйте ввести ще раз."
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(f'{self.magenta}{message}')
                continue
        print()
        while True:
            message = f'Введіть шлях до файла, до якого записувати результат у вигляді D:\myfiles\welcome.txt, \nякщо бажаєте повернутись назад, введіть "назад": '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}', end = '')
            output_file = input(self.cyan)
            self.dialog.append(('User', output_file, datetime.datetime.now().strftime('%H:%M:%S')))
            if output_file == 'назад': return
            try:
                with open(output_file, 'w', encoding='utf-8') as file:
                    for line in reversed_lines:
                        file.write(line)
                    break
            except:
                message = f"Не вдалося записати до файлу '{output_file}', спробуйте ввести ще раз."
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(f'{self.magenta}{message}')
                continue
        message =f"\nВміст файлу {input_file} в зворотному порядку збережено до файлу {output_file}"
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

    def lowercase(self):
        while True:
            message = f'Введіть шлях до файла, з яким необхідно працювати у вигляді D:\myfiles\welcome.txt, \nякщо бажаєте повернутись назад, введіть "назад": '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}', end = '')
            input_file = input(self.cyan)
            self.dialog.append(('User', input_file, datetime.datetime.now().strftime('%H:%M:%S')))
            if input_file == 'назад': return
            try:
                with open(input_file, 'r', encoding='utf-8') as file:
                    text = file.read()
                    lowercase_text = text.lower()
                    break
            except FileNotFoundError:
                message = f"Файл '{input_file}' не знайдено, спробуйте ввести ще раз."
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(f'{self.magenta}{message}')
                continue
        print()
        while True:
            message = f'Введіть шлях до файла, до якого записувати результат у вигляді D:\myfiles\welcome.txt, \nякщо бажаєте повернутись назад, введіть "назад": '
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}', end = '')
            output_file = input(self.cyan)
            self.dialog.append(('User', output_file, datetime.datetime.now().strftime('%H:%M:%S')))
            if output_file == 'назад': return
            try:
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(lowercase_text)
                    break
            except:
                message = f"Не вдалося записати до файлу '{output_file}', спробуйте ввести ще раз."
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(f'{self.magenta}{message}')
                continue
        message =f"\nВміст файлу {input_file} у нижньому регістрі збережено до файлу {output_file}"
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')
        
    def common(self):
        message = random.choice(self.responses['вставочки'])
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(message)
        while True:
            message = '''\nОбрано розділ "загальне". Оберіть питання з перерахованих (напишіть його номер), 
якщо бажаєте повернутись до головного меню, введіть "назад":
        1. Яка зараз пора року?
        2. Як тебе звати?  : '''
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}')
            subtopic = input(self.cyan).lower().strip('./@#$%^&*()_+=')
            self.dialog.append(('User', subtopic, datetime.datetime.now().strftime('%H:%M:%S')))

            if subtopic == '1':
                self.get_current_season()

            elif subtopic == '2':
                self.get_name()

            elif subtopic == 'назад':
                break

            else:
                message = random.choice(self.responses['ерор'])
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message)
                continue

    def get_current_season(self):
        now = datetime.datetime.now()
        month = now.month
        season = ""

        if month in [12, 1, 2]:
            season = "зима"
        elif month in [3, 4, 5]:
            season = "весна"
        elif month in [6, 7, 8]:
            season = "літо"
        elif month in [9, 10, 11]:
            season = "осінь"

        message = f"Зараз {season}."
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

    def get_name(self):
        message = 'Мене звати бот Володька.'
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

    def others(self):
        message = random.choice(self.responses['вставочки'])
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(message)
        while True:
            message = '''\nОбрано розділ "інше". Оберіть питання з перерахованих (напишіть його номер), 
якщо бажаєте повернутись до головного меню, введіть "назад":
        1. Хочу отримати мотивуючу цитату
        2. Хочу дізнатись ймовірність події  : '''
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}')
            subtopic = input(self.cyan).lower().strip('./@#$%^&*()_+=')
            self.dialog.append(('User', subtopic, datetime.datetime.now().strftime('%H:%M:%S')))

            if subtopic == '1':
                self.get_random_quote()

            elif subtopic == '2':
                self.possibility()

            elif subtopic == 'назад':
                break

            else:
                message = random.choice(self.responses['ерор'])
                self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
                print(message)
                continue

    def get_random_quote(self):
        self.quotes = [
            "Секрет успіху - почати діяти.",
            "Нехай кожен день буде новим кроком до великої перемоги.",
            "Ви можете досягти всього, що забажаєте, якщо вірите в себе.",
            "Перемога належить тим, хто вірить в себе.",
            "Ваші мрії варті зусиль. Не зупиняйтесь!"]
        quote = random.choice(self.quotes)
        message = f"Мотивуюча цитата для вас: {quote}"
        self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
        print(f'{self.magenta}{message}')

    def possibility(self):
        while True :
            message = '''\nПоставте мені питання типу "яка ймовірність того-то", якщо бажаєте повернутися до попереднього меню, введіть "назад": '''
            self.dialog.append(('Bot', message, datetime.datetime.now().strftime('%H:%M:%S')))
            print(f'{self.magenta}{message}')
            question = input(self.cyan).lower().strip('./@#$%^&*()_+=')
            self.dialog.append(('User', question, datetime.datetime.now().strftime('%H:%M:%S')))
            if question == 'назад': return
            else:
                answer = f"Ймовірність цього: {round(random.uniform(1, 100),2)} %"
                self.dialog.append(('Bot', answer, datetime.datetime.now().strftime('%H:%M:%S')))
                print(f'{self.magenta}{answer}')
                break
 
    def save_dialog(self):
        current_time = datetime.datetime.now()
        filename = f'dialog-{current_time.strftime("%Y-%m-%d_%H-%M-%S")}.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            for speaker, message, time in self.dialog:                     
                file.write(f'{speaker}:  {message} - {time}\n')
        print(f"Діалог збережено до файлу {filename}")

bot = Bot()
bot.greet()
bot.select_topic()
bot.save_dialog()