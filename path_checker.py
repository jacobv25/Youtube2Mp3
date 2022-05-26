import os


class PathChecker:
    def __init__(self, path):
        self.path = path

    def set_path(self, path):
        self.path = path

    def check_dir_path(self):
        return os.path.isdir(self.path)

if __name__ == '__main__':
    checker = PathChecker(r'D:\Music')
    result = checker.check_dir_path()
    print(f'result = {result}')
    checker.set_path(r'C:\Users\javal\Music')
    result = checker.check_dir_path()
    print(f'result = {result}')