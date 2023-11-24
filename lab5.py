"""
The program prints a file tree and the longest path, 
creates a file system from subfolders and files
"""


class File:
    """
    This class returns name, extension and size of a file and calls destructor 
    """

    def __init__(self, name="dsf", extension="png", size="234 mb"):
        self.name = name
        self.extension = extension
        self.size = size

    def get_name(self):
        """
        Method returns name of folder
        """
        return self.name

    def get_extension(self):
        """
        Method returns extension of file
        """
        return self.extension

    def get_size(self):
        """
        Method returns size of file
        """
        return self.size

    def __str__(self):
        return f'{self.get_name()}.{self.get_extension()}, {self.get_size()}'

    def __del__(self):
        return f"Файл {self.get_name()} було видалено"


class Folder:
    """
    The class realises adding files and folders, outputting a file tree,
    finding the longest path and calls destructor
    """

    def __init__(self, name):
        self.name = name
        self.path = []

    def get_name(self):
        """
        Method returns name of folder
        """
        return self.name

    def add(self, item):
        """
        Method adds file to the folder and adds folder to the folder
        """
        self.path.append(item)

    def __str__(self):
        return self.get_name()

    def longest_path(self):
        """
        Method finds the longest path to the file and prints it 
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
        Method prints file tree
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
    This method initializes the objects, outputs the input values ​​in 
    a file tree format, and outputs the longest path to the file
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

    folder_main.tree()

    print(f'Найдовший шлях: {folder_main.longest_path()}')


main()
