import random  # Importuje modul 'random' pro generování náhodných čísel

START_POINT = 1  # Výchozí bod pro všechny hráče
END_POINT = 100  # Konečný bod (cílová pozice)

class Player:  # Třída reprezentující hráče
    def __init__(self, name, colour):  # Inicializuje objekt hráče s jménem a barvou
        self.name = name  # Přiřazuje jméno hráči
        self.position = START_POINT  # Nastavuje výchozí pozici hráče
        self.colour = Player.colour_code(colour)  # Nastavuje barvu hráče pomocí metody 'colour_code'

    @staticmethod
    def colour_code(colour):  # Statická metoda pro mapování zkratky barvy na ANSI kód barvy
        colour_mapping = {
            'r': 31,  # Červená
            'g': 32,  # Zelená
            'b': 34,  # Modrá
            'y': 33,  # Žlutá
        }
        return colour_mapping.get(colour, 37)  # Vrátí odpovídající kód nebo bílou, pokud je barva neplatná

    def move(self, spaces):  # Metoda pro pohyb hráče o zadaný počet políček
        self.position += spaces  # Zvyšuje pozici hráče o hodnotu 'spaces'

    def __str__(self):  # Přetížení metody __str__ pro reprezentaci objektu jako textu
        return f"{self.name} is on position {self.position}"  # Vrací textovou reprezentaci pozice hráče

    def print_player(self):  # Tiskne jméno hráče a jeho pozici v jeho barvě
        print(f"\033[{self.colour}m{self.name}\033[0m is on position \033[{self.colour}m{self.position}\033[0m")

class Game:  # Třída reprezentující samotnou hru
    game_count = 0  # Statická proměnná pro sledování počtu her

    @staticmethod
    def get_number_of_players():  # Metoda pro získání počtu hráčů od uživatele
        while True:  # Nekonečná smyčka, dokud není zadán platný počet hráčů
            try:
                num_players = int(input("Enter the number of players (\033[34m1 \033[0m- \033[31m4\033[0m): "))  # Ptá se uživatele na počet hráčů
                if 0 < num_players <= 4:  # Kontroluje, zda je počet hráčů v rozsahu 1 až 4
                    return num_players  # Pokud ano, vrací tento počet
                else:
                    print("Number of players must be greater than 0 and less than or equal to 4. Please try again.")  # Chybová zpráva při neplatném počtu hráčů
            except ValueError:
                print("Invalid input. Please enter a valid number.")  # Chybová zpráva při neplatném vstupu

    @staticmethod
    def create_player(available_colors, used_names, used_colors, i):  # Metoda pro vytvoření hráče
        name = input(f"Please enter player {i}'s name: ").strip()  # Ptá se na jméno hráče
        while name in used_names:  # Zkontroluje, zda jméno nebylo již použito
            print("Name already taken. Please choose a different name.")  # Chybová zpráva při opakovaném jméně
            name = input(f"Please enter player {i}'s name: ").strip()  # Znovu požaduje jméno

        color = input(f"Please enter player {i}'s color (r - red, g - green, b - blue, y - yellow): ").strip().lower()  # Ptá se na barvu hráče
        while color not in available_colors or color in used_colors:  # Zkontroluje, zda je barva platná a nepoužitá
            if color not in available_colors:
                print("Invalid color. Please choose a valid color.")  # Chybová zpráva při neplatné barvě
            else:
                print("Color already taken. Please choose a different color.")  # Chybová zpráva, pokud je barva již zabraná
            color = input(f"Please enter player {i}'s color (r - red, g - green, b - blue, y - yellow): ").strip().lower()  # Znovu požaduje barvu

        used_names.add(name)  # Přidává jméno do množiny použitých jmen
        used_colors.add(color)  # Přidává barvu do množiny použitých barev
        return name, color  # Vrací jméno a barvu hráče

    def __init__(self):  # Konstruktor třídy Game
        self.players = []  # Inicializuje prázdný seznam hráčů
        self.current_player_index = 0  # Inicializuje index aktuálního hráče
        Game.game_count += 1  # Zvyšuje počet her

        # Slovník s polohami hadů
        self.snakes = {
            16: 6,
            47: 26,
            49: 11,
            56: 53,
            62: 19,
            64: 60,
            87: 24,
            93: 73,
            95: 75,
            98: 78
        }
        # Slovník s polohami žebříků
        self.ladders = {
            2: 38,
            4: 14,
            9: 31,
            21: 42,
            28: 84,
            36: 44,
            51: 67,
            71: 91,
            80: 100
        }

    @staticmethod
    def roll_dice():  # Metoda pro hod kostkou
        return random.randint(1, 6)  # Vrací náhodné číslo mezi 1 a 6

    def add_player(self, name, colour):  # Přidává hráče do hry
        player = Player(name, colour)  # Vytváří nového hráče
        self.players.append(player)  # Přidává hráče do seznamu hráčů

    def check_snakes_and_ladders(self, player):  # Kontroluje, zda hráč narazil na hada nebo žebřík
        if player.position in self.ladders:  # Kontrola, zda je hráč na pozici žebříku
            print(f"{player.name} found a ladder! Climbing up to {self.ladders[player.position]}")  # Informuje hráče, že našel žebřík
            player.position = self.ladders[player.position]  # Přesune hráče nahoru
        elif player.position in self.snakes:  # Kontrola, zda je hráč na pozici hada
            print(f"{player.name} got bitten by a snake! Sliding down to {self.snakes[player.position]}")  # Informuje hráče, že ho pokousal had
            player.position = self.snakes[player.position]  # Přesune hráče dolů

    def check_for_other_players(self, current_player):  # Kontroluje, zda je na pozici jiný hráč
        for player in self.players:
            if player != current_player and player.position == current_player.position:  # Pokud je jiný hráč na stejné pozici
                print(f"\033[{player.colour}m{player.name}\033[0m is already on position {player.position}. "
                      f"Moving \033[{player.colour}m{player.name}\033[0m back by 1 space.")  # Informuje hráče
                player.move(-1)  # Pohne jiným hráčem zpět o 1 pozici
                self.check_snakes_and_ladders(player)  # Znovu zkontroluje hady a žebříky
                self.check_for_other_players(player)  # Znovu zkontroluje další hráče

    def play_game(self):  # Hlavní herní smyčka
        is_winner = False  # Kontrola, zda už je vítěz
        while not is_winner:  # Smyčka běží, dokud není vítěz
            current_player = self.players[self.current_player_index]  # Vybere aktuálního hráče
            input(f"\033[{current_player.colour}m{current_player.name}\033[0m, press Enter to roll the dice.")  # Požaduje od hráče stisknutí klávesy Enter
            roll = self.roll_dice()  # Hráč hodí kostkou
            total_roll = roll  # Nastaví hod kostkou jako počáteční hodnotu

            while roll == 6:  # Pokud hráč hodí šestku
                print(f"\033[{current_player.colour}m{current_player.name}\033[0m rolled a 6! Roll again.")  # Informuje hráče, že hodil 6
                input(f"\033[{current_player.colour}m{current_player.name}\033[0m, press Enter to roll the dice.")  # Hráč hází znovu
                roll = self.roll_dice()  # Další hod
                total_roll += roll  # Přičte další hod k celkovému

                if total_roll - roll == 18:  # Pokud hráč hodí třikrát 6 po sobě
                    print(f"\033[{current_player.colour}m{current_player.name}\033[0m rolled three 6s in a row. Turn forfeited!")  # Informuje hráče, že ztratil tah
                    total_roll = 0  # Nastaví tah na 0
                    break  # Ukončí smyčku

            print(f"\033[{current_player.colour}m{current_player.name}\033[0m rolled a total of \033[{current_player.colour}m{total_roll}\033[0m")  # Informuje hráče o celkovém hodu

            if current_player.position + total_roll > END_POINT:  # Pokud by se hráč dostal mimo konec hracího pole
                print(f"\033[{current_player.colour}m{current_player.name}\033[0m, you cannot move, as you would exceed {END_POINT}.")  # Informuje hráče, že nemůže pokračovat
            else:
                current_player.move(total_roll)  # Pohne hráčem o počet políček odpovídající hodu

            self.check_for_other_players(current_player)  # Zkontroluje, zda je na pozici jiný hráč
            self.check_snakes_and_ladders(current_player)  # Zkontroluje, zda hráč nenarazil na hada nebo žebřík
            current_player.print_player()  # Vytiskne stav hráče

            if current_player.position == END_POINT:  # Pokud hráč dosáhne cíle
                print(f"\n\033[{current_player.colour}m{current_player.name}\033[0m wins! CONGRATULATIONS!!!\n")  # Informuje, že hráč vyhrál
                is_winner = True  # Nastaví, že je vítěz

            self.current_player_index = (self.current_player_index + 1) % len(self.players)  # Přesune tah na dalšího hráče

    def start_game(self):  # Metoda pro spuštění hry
        print(f'\n\033[34mWelcome to \033[31msnakes\033[32m and \033[33mladders \033[0mgame !!!\n')  # Uvítací zpráva

        num_players = self.get_number_of_players()  # Získá počet hráčů
        available_colors = {'r', 'g', 'b', 'y'}  # Dostupné barvy
        used_colors = set()  # Množina použitých barev
        used_names = set()  # Množina použitých jmen

        for i in range(1, num_players + 1):  # Smyčka pro vytvoření hráčů
            name, color = self.create_player(available_colors, used_names, used_colors, i)  # Vytvoří hráče
            self.add_player(name, color)  # Přidá hráče do hry

        for player in self.players:  # Vytiskne stav každého hráče
            player.print_player()

        self.play_game()  # Spustí herní smyčku

game = Game()  # Vytvoří instanci hry
game.start_game()  # Spustí hru
