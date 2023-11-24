"""
Програма реалізує вивід дерева файлів, найдовший шлях до файлу
та викликає деструктори файлів і папок
"""


class File:
    """
    Реалізує створення файлів
    """

    def __init__(self, name="dsf", extension="png", size="234 mb"):
        self.name = name
        self.extension = extension
        self.size = size

    def get_name(self):
        """
        Дістає ім'я файлу
        """
        return self.name

    def get_extension(self):
        """
        Дістає розширення файлу
        """
        return self.extension

    def get_size(self):
        """
        Дістає розмір файлу
        """
        return self.size

    def __str__(self):
        return f'{self.get_name()}.{self.get_extension()}, {self.get_size()}'

    def __del__(self):
        return f"Файл {self.get_name()} було видалено"


class Folder:
    """
    Реалізує додавання файлів та папок, вивід дерева файлів та
    знаходження найдовшого шляху
    """

    def __init__(self, name):
        self.name = name
        self.path = []

    def get_name(self):
        """
        Дістає назву папки
        """
        return self.name

    def add(self, item):
        """
        Додає файли або папки до папок
        """
        self.path.append(item)

    def __str__(self):
        return self.get_name()

    def longest_path(self):
        """
        Знаходить найдовший шлях та виводить його
        """
        long_path = ""
        for item in self.path:
            if isinstance(item, File):
                if len(item.name) > len(long_path):
                    long_path = item.name
            elif isinstance(item, Folder):
                folder_path = item.name + "/" + item.longest_path()
                if len(folder_path) > len(long_path):
                    long_path = folder_path
        return long_path

    def tree(self, indent=''):
        """
        Виводить дерево файлів
        """
        print(indent + self.get_name() + "/")
        for item in self.path:
            if isinstance(item, File):
                print(indent + "    " + str(item))
            elif isinstance(item, Folder):
                item.tree(indent + "    ")

    def __del__(self):
        return f"Папку {self.get_name()} було видалено"


def main():
    """
    Ініціалізатор об'єктів та вивід введених значень
    """
    folder_main = Folder("main")

    folder_projects = Folder("Projects")
    file_car = File("Car", 'png', '657 mb')

    folder_hw = Folder("Hw")
    folder_math = Folder('Math')
    file_1 = File('1', 'pdf', '50 mb')
    file_bio = File('Bio', 'txt', '40 mb')

    folder_labs = Folder('Labs')
    folder_lab_1 = Folder('lab1')
    folder_physics = Folder('Physics')
    file_graphics = File('Graphics', 'png', '20mb')
    folder_lab_2 = Folder('lab2')
    folder_python = Folder('Python')
    folder_code = Folder('code')
    file_lab_2_code = File('lab2_code', 'py', '2 mb')

    folder_main.add(folder_projects)
    folder_projects.add(file_car)

    folder_main.add(folder_hw)
    folder_hw.add(file_bio)

    folder_hw.add(folder_math)
    folder_math.add(file_1)

    folder_main.add(folder_labs)

    folder_labs.add(folder_lab_1)
    folder_lab_1.add(folder_physics)
    folder_physics.add(file_graphics)

    folder_labs.add(folder_lab_2)

    folder_lab_2.add(folder_python)

    folder_python.add(folder_code)
    folder_code.add(file_lab_2_code)

    folder_main.print_tree()

    print(f'Найдовший шлях: {folder_main.longest_path()}')


main()
