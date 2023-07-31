class Character():

    def __init__(self):
        self.name = ""
        self.race = ""
        self.outfit = {
            "helmet" : "",
            'Chestplate' : '',
            'pants': '',
            'boots': ''
        }
    
    def get_info(self, name, race):
        pass

    def change_boots(self, boots):
        pass

    def change_pants(self, pants):
        pass
    
    def get_armor(self):
        pass

    def change_helm(self, helm):
        pass

    def change_plate(slef, plate):
        pass

    def display_outfit(self):
        print('you are currently wwearing:')
        
    def runner(self):
        print('-----Welcome to the character builder!------')
        name = input('What is your name? ')
        race = input('What race are you?')
        self.get_info(name, race)

        print(f'Welcome, {self.name}')
        print('Lets customizer yoru gear')
        while True:
            response = input('would you like to view your fit, or edit, or save?')
            if response.lower() == 'view':