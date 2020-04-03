import argparse
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_dt_from_file(filename: str):
    dt = filename.split('/')[-1]
    return float(dt.split('_alpha')[0].split('=')[-1])


def plot_results(folder: str):
    files = glob.glob(folder + "/*.csv")
    i = 1
    for filename in files:
        df = pd.read_csv(filename, index_col=None, header=0)
        df.columns = ['prey', 'predator']

        dt = get_dt_from_file(filename)
        time = np.arange(len(df.index) * dt, step=dt)
        plt.plot(time, df.prey, label=f'prey {i}')
        plt.plot(time, df.predator, label=f'predator {i}')
        i += 1
    plt.xlabel('t')
    plt.ylabel('population')
    # plt.legend()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot simulation results')
    parser.add_argument('--folder_name', type=str,
                        help='Folder name', required=True)
    results = parser.parse_args()
    plot_results(results.folder_name)
