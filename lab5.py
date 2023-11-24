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
    folder1 = Folder("main")

    folder2 = Folder("Projects")
    file1 = File("Car", 'png', '657 mb')

    folder3 = Folder("Hw")
    folder5 = Folder('Math')
    file4 = File('1', 'pdf', '50 mb')
    file6 = File('Bio', 'txt', '40 mb')

    folder4 = Folder('Labs')
    folder6 = Folder('lab1')
    folder8 = Folder('Physics')
    file8 = File('1', 'png', '20mb')
    folder7 = Folder('lab2')
    folder9 = Folder('Python')
    folder11 = Folder('code')
    file13 = File('lab2_code', 'py', '2 mb')

    folder1.add(folder2)
    folder2.add(file1)

    folder1.add(folder3)
    folder3.add(file6)

    folder3.add(folder5)
    folder5.add(file4)

    folder1.add(folder4)

    folder4.add(folder6)
    folder6.add(folder8)
    folder8.add(file8)

    folder4.add(folder7)

    folder7.add(folder9)

    folder9.add(folder11)
    folder11.add(file13)

    folder1.tree()

    print(f'Найдовший шлях: {folder1.longest_path()}')


main()
