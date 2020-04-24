import argparse
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import animation


def get_dt_from_file(filename: str):
    dt = filename.split('/')[-1]
    return float(dt.split('_alpha')[0].split('=')[-1])


def load_datasets(folder: str):
    files = glob.glob(folder + "/*.csv")
    if len(files) < 1:
        print(f"Not found datasets in [{folder}]")
        return
    dfs = []
    for filename in files:
        df = pd.read_csv(filename, index_col=None, header=0)
        df.columns = ['prey', 'predator']
        dt = get_dt_from_file(filename)
        time = np.arange(len(df.index) * dt, step=dt)
        dfs.append(pd.DataFrame(
            {'time': time, 'prey': df.prey, 'predator': df.predator}))
    return dfs


def get_x_lim(df):
    return np.min(df.time), np.max(df.time)


def get_y_lim(dfs):
    y_min = []
    y_max = []
    for df in dfs:
        y_min.append(np.min([np.min(df.prey), np.min(df.predator)]))
        y_max.append(np.max([np.max(df.prey), np.max(df.predator)]))
    return np.min(y_min), np.max(y_max)


def animate_results(folder: str, anim_name: str):
    dfs = load_datasets(folder)

    def animate(i):
        plt.clf()
        plt.xlim(get_x_lim(dfs[0]))
        plt.ylim(get_y_lim(dfs))
        for num, df in enumerate(dfs[:5]):
            plt.plot(df.time[:(i * 10)], df.prey[:(i * 10)],
                     label=f'prey {num}')
            plt.plot(df.time[:(i * 10)], df.predator[:(i * 10)],
                     label=f'predator {num}')
        plt.legend(loc='upper left')
        plt.xlabel('time')
        plt.ylabel('population')
    fig, ax = plt.subplots(figsize=(10, 8))
    anim = animation.FuncAnimation(fig, animate, frames=(int)(len(
        dfs[0].time) / 10), interval=10, repeat=True)
    anim.save(anim_name + '.gif', writer='imagemagick')


def plot_results(folder: str):
    dfs = load_datasets(folder)
    for i, df in enumerate(dfs):
        plt.plot(df.time, df.prey, label=f'prey {i + 1}')
        plt.plot(df.time, df.predator, label=f'predator {i + 1}')
    plt.xlabel('t')
    plt.ylabel('population')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot simulation results')
    parser.add_argument('--folder_name', type=str,
                        help='Folder name', required=True)
    results = parser.parse_args()
    # plot_results(results.folder_name)
    animate_results(results.folder_name, 'stochastic')
