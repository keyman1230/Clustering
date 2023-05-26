import sys
sys.path.append("D:\# Shared_Folder_HDD\# Python_Code_and_Tool\github-repo\# Jayce")
from log import log
from file_control import untitled as fc


def clustering():
    pass
def indexing():
    pass

if __name__ == "__main__":
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    # setting log
    logger = log.set_log(module="Indexing", lv="INFO")
    # logger.info("test log")

    path = fc.select_file(init_dir="./")
    df = pd.read_excel(path)
    logger.info(f"path : {path}")
    plt.figure()
    sns.scatterplot(data=df, x="Marker_Center_X_full", y="Marker_Center_Y_full")
    plt.savefig("test.png")
