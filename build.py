#!python3
import os, sys
import zipfile

if __name__ == '__main__':
    try:
        os.unlink("HeatMap.zip")
    except FileNotFoundError:
        pass

    with zipfile.ZipFile("HeatMap.zip", "w") as z:
        cwd = os.getcwd()
        os.chdir("bi-irregular-2dim-heatmap")
        try:
            for dirpath, dirnames, filenames in os.walk("."):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    print(filepath)
                    z.write(filepath)
        finally:
            os.chdir(cwd)

    input("Press enter to continue...")