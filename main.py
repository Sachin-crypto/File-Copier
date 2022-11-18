import shutil
import os
from prettytable import PrettyTable

source = input("Enter the source path: ")
print("Data source: ", source)
destination = input("Enter the destination path: ")
print("Data will be copied to: ", destination)

try:
    if os.path.isdir(destination):
        print("Uh-oh, destination path already exists.")
    else:
        copy_tree = shutil.copytree(source, destination)
        print(f"Directory copied to: {destination}")

        file_names = []
        for files in os.listdir(destination):
            file_names.append(
                [destination, files]
            )

        table = PrettyTable(
            field_names=["Destination", "Files"]
        )
        table.add_rows(file_names)
        print(table)
except:
    print("Cannot process the request. Specify legal path of directory.")
