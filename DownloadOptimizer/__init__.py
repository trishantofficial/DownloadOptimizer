from multiprocessing import freeze_support
from DownloadOptimizer import main as DL
from CheckModules import initialSetup
if __name__ == '__main__':
    freeze_support()
    initialSetup()
    DL()