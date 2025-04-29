''' 
To treat individual objects and compositions of objects uniformly

Component: Base class/interface for all objects in the composition.
Leaf: Represents individual objects.
Composite: Stores child components and implements child-related operations.
'''

from abc import ABC, abstractmethod

# Abstract base class 
class FileSystemEntity(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Leaf node 
class File(FileSystemEntity):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print('  ' * indent + f'File: {self.name}')

# Composite node 
class Directory(FileSystemEntity):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, entity: FileSystemEntity):
        self.children.append(entity)

    def remove(self, entity: FileSystemEntity):
        self.children.remove(entity)

    def display(self, indent=0):
        print('  ' * indent + f'Directory: {self.name}')
        for child in self.children:
            child.display(indent + 1)

# Client code
root = Directory("root")
root.add(File("file1.txt"))
root.add(File("file2.txt"))

sub_dir = Directory("subdir")
sub_dir.add(File("file3.txt"))

root.add(sub_dir)

root.display()
'''
Directory: root
  File: file1.txt
  File: file2.txt
  Directory: subdir
    File: file3.txt
'''