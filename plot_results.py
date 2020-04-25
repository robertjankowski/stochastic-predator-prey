import argparse
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import animation, rcParams, cycler

cmap = plt.cm.jet


def get_dt_from_file(filename: str):
    dt = filename.split("/")[-1]
    return float(dt.split("_alpha")[0].split("=")[-1])


def load_datasets(folder: str, n_obs: int) -> list:
    files = glob.glob(folder + "/*.csv")
    if len(files) < 1:
        print(f"Not found datasets in [{folder}]")
        return
    dfs = []
    for filename in files:
        df = pd.read_csv(filename, index_col=None, header=0)
        df.columns = ["prey", "predator"]
        dt = get_dt_from_file(filename)
        time = np.arange(len(df.index) * dt, step=dt)
        dfs.append(
            pd.DataFrame({"time": time, "prey": df.prey, "predator": df.predator})
        )
    return dfs[:n_obs]


def get_x_lim(df):
    return np.min(df.time), np.max(df.time)


def get_y_lim(dfs):
    y_min = []
    y_max = []
    for df in dfs:
        y_min.append(np.min([np.min(df.prey), np.min(df.predator)]))
        y_max.append(np.max([np.max(df.prey), np.max(df.predator)]))
    return np.min(y_min), np.max(y_max)


def animate_results(folder: str, anim_name: str, n_obs: int):
    dfs = load_datasets(folder, n_obs)

    def animate(i):
        plt.clf()
        plt.xlim(get_x_lim(dfs[0]))
        plt.ylim(get_y_lim(dfs))
        for num, df in enumerate(dfs[:5]):
            plt.plot(df.time[: (i * 10)], df.prey[: (i * 10)], label=f"prey {num}")
            plt.plot(
                df.time[: (i * 10)], df.predator[: (i * 10)], label=f"predator {num}"
            )
        plt.legend(loc="upper left")
        plt.xlabel("time")
        plt.ylabel("population")

    fig, ax = plt.subplots(figsize=(10, 8))
    anim = animation.FuncAnimation(
        fig, animate, frames=(int)(len(dfs[0].time) / 10), interval=10, repeat=True
    )
    anim.save(anim_name + ".gif", writer="imagemagick")


def plot_results_deterministic(df_deterministic):
    plt.plot(
        df_deterministic.time,
        df_deterministic.prey,
        label="deterministic prey",
        color="black",
        linewidth=2.5,
    )
    plt.plot(
        df_deterministic.time,
        df_deterministic.predator,
        label="deterministic predator",
        color="red",
        linewidth=2.5,
    )


def plot_results(stochastic_folder: str, deterministic_folder: str, n_obs: int):
    dfs = load_datasets(stochastic_folder, n_obs)
    for i, df in enumerate(dfs):
        plt.plot(df.time, df.prey, label=f"stochastic prey {i + 1}")
        plt.plot(df.time, df.predator, label=f"stochastic predator {i + 1}")
    df_deterministic = load_datasets(deterministic_folder, 1)[0]
    plot_results_deterministic(df_deterministic)
    plt.xlabel("t")
    plt.ylabel("population")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot simulation results")
    parser.add_argument(
        "--stochastic_folder_name",
        type=str,
        help="Name of folder with stochastic solution",
        required=True,
    )
    parser.add_argument(
        "--n_obs_stochastic", type=int, help="Number of stochastic runs", required=True
    )
    parser.add_argument(
        "--deterministic_folder_name",
        type=str,
        help="Name of folder with deterministic solution",
        required=True,
    )

    results = parser.parse_args()
    stochastic_folder = results.stochastic_folder_name
    n_obs = results.n_obs_stochastic
    deterministic_folder = results.deterministic_folder_name

    plot_results(stochastic_folder, deterministic_folder, n_obs)
    # animate_results(results.folder_name, 'stochastic')
