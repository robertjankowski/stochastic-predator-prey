import argparse
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import animation, rcParams, cycler

cmap = plt.cm.jet


def get_files_from(folder: str):
    files = glob.glob(folder + "/*.csv")
    if not files:
        print(f"Cannot load files from: [{folder}]. Folder is empty.")
        return
    return files


def get_sigma_x_y(stochastic_folder: str):
    file = get_files_from(stochastic_folder)[0]
    sigmas = file.split('sigma_x=')[1].split('_sigma_y=')
    sigma_x = sigmas[0]
    sigma_y = sigmas[1].split('_')[0]
    return sigma_x, sigma_y


def get_lotka_volterra_params(stochastic_folder: str):
    file = get_files_from(stochastic_folder)[0]
    params = file.split('_alpha=')[1].split('_beta=')
    alpha = params[0]
    params = params[1].split('_delta=')
    beta = params[0]
    params = params[1].split('_gamma=')
    delta = params[0]
    params = params[1].split('_sigma_x=')
    gamma = params[0]
    return alpha, beta, delta, gamma


def get_dt_from_file(filename: str):
    dt = filename.split("/")[-1]
    return float(dt.split("_alpha")[0].split("=")[-1])


def load_datasets(folder: str, n_obs: int) -> list:
    dfs = []
    for filename in get_files_from(folder):
        df = pd.read_csv(filename, index_col=None, header=0)
        df.columns = ["prey", "predator"]
        dt = get_dt_from_file(filename)
        time = np.arange(len(df.index) * dt, step=dt)
        dfs.append(pd.DataFrame({"time": time, "prey": df.prey,
                                 "predator": df.predator}))
    return dfs[:n_obs]


def get_x_lim(df):
    return np.min(df.time), np.max(df.time)


def get_y_lim(dfs, df_deterministic):
    y_min = []
    y_max = []
    for df in dfs:
        y_min.append(df[["prey", "predator"]].min())
        y_max.append(df[["prey", "predator"]].max())
    y_min.append(df_deterministic[["prey", "predator"]].min())
    y_max.append(df_deterministic[["prey", "predator"]].max())
    return np.min(y_min), np.max(y_max)


def animate_results(stochastic_folder: str, deterministic_folder: str, n_obs: int):
    dfs = load_datasets(stochastic_folder, n_obs)
    df_deterministic = load_datasets(deterministic_folder, 1)[0]
    sigma_x, sigma_y = get_sigma_x_y(stochastic_folder)
    alpha, beta, delta, gamma = get_lotka_volterra_params(stochastic_folder)

    def animate(i):
        plt.clf()
        plt.xlim(get_x_lim(dfs[0]))
        plt.ylim(get_y_lim(dfs, df_deterministic))
        for num, df in enumerate(dfs):
            plt.plot(df.time[: (i * 10)],
                     df.prey[: (i * 10)], label=f"stochastic prey {num + 1}")
            plt.plot(df.time[: (i * 10)],
                     df.predator[: (i * 10)], label=f"stochastic predator {num + 1}")
        plt.plot(
            df_deterministic.time[: (i * 10)],
            df_deterministic.prey[: (i * 10)],
            label="deterministic prey",
            color="black",
            linewidth=2.5
        )
        plt.plot(
            df_deterministic.time[: (i * 10)],
            df_deterministic.predator[: (i * 10)],
            label="deterministic predator",
            color="red",
            linewidth=2.5
        )
        plt.legend(loc="upper right")
        plt.xlabel("time")
        plt.title(r'$\alpha = {}, \beta = {}, \delta = {}, \gamma = {}, \sigma_x = {}, \sigma_y = {}$'.format(
            alpha, beta, delta, gamma, sigma_x, sigma_y))
        plt.ylabel("population")
    fig, ax = plt.subplots(figsize=(10, 6))
    anim = animation.FuncAnimation(
        fig, animate, frames=(int)(len(dfs[0].time) / 10), interval=5, repeat=True
    )
    anim.save(
        'animation_alpha={}_beta={}_delta={}_gamma={}_sigma_x={}_sigma_y={}.gif'.format(
            alpha, beta, delta, gamma, sigma_x, sigma_y),
        writer="imagemagick")


def plot_results_deterministic(df_deterministic):
    plt.plot(
        df_deterministic.time,
        df_deterministic.prey,
        label="deterministic prey",
        color="black",
        linewidth=2.5
    )
    plt.plot(
        df_deterministic.time,
        df_deterministic.predator,
        label="deterministic predator",
        color="red",
        linewidth=2.5
    )


def plot_results(stochastic_folder: str, deterministic_folder: str, n_obs: int, savefig=False):
    dfs = load_datasets(stochastic_folder, n_obs)
    df_deterministic = load_datasets(deterministic_folder, 1)[0]
    sigma_x, sigma_y = get_sigma_x_y(stochastic_folder)
    alpha, beta, delta, gamma = get_lotka_volterra_params(stochastic_folder)

    plt.figure(figsize=(10, 6))
    for i, df in enumerate(dfs):
        plt.plot(df.time, df.prey, label=f"stochastic prey {i + 1}")
        plt.plot(df.time, df.predator, label=f"stochastic predator {i + 1}")
    plot_results_deterministic(df_deterministic)
    plt.xlabel("t")
    plt.ylabel("population")
    plt.title(r'$\alpha = {}, \beta = {}, \delta = {}, \gamma = {}, \sigma_x = {}, \sigma_y = {}$'.format(
        alpha, beta, delta, gamma, sigma_x, sigma_y))
    plt.legend(loc='upper left')
    if savefig:
        plt.savefig(
            'figures/alpha={}_beta={}_delta={}_gamma={}_sigma_x={}_sigma_y={}.pdf'.format(
                alpha, beta, delta, gamma, sigma_x, sigma_y),
            bbox_inches='tight')
    else:
        plt.show()


def plot_phase_space(stochastic_folder: str, deterministic_folder: str, n_obs: int, savefig=False):
    dfs = load_datasets(stochastic_folder, n_obs)
    df_deterministic = load_datasets(deterministic_folder, 1)[0]
    sigma_x, sigma_y = get_sigma_x_y(stochastic_folder)
    alpha, beta, delta, gamma = get_lotka_volterra_params(stochastic_folder)

    plt.figure(figsize=(10, 6))
    for i, df in enumerate(dfs):
        plt.plot(df.prey, df.predator,
                 label=f"stochastic prey vs predator {i + 1}")
    plt.plot(
        df_deterministic.prey,
        df_deterministic.predator,
        label="deterministic prey vs predator",
        color="black",
        linewidth=2.5
    )
    plt.xlabel("# prey")
    plt.ylabel("# predator")
    plt.title(r'$\alpha = {}, \beta = {}, \delta = {}, \gamma = {}, \sigma_x = {}, \sigma_y = {}$'.format(
        alpha, beta, delta, gamma, sigma_x, sigma_y))
    plt.legend()
    if savefig:
        plt.savefig(
            'figures/phase_diagram_alpha={}_beta={}_delta={}_gamma={}_sigma_x={}_sigma_y={}.pdf'.format(
                alpha, beta, delta, gamma, sigma_x, sigma_y),
            bbox_inches='tight')
    else:
        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot simulation results")
    parser.add_argument(
        "--stochastic_folder_name",
        type=str,
        help="Name of the folder with stochastic solutions",
        required=True,
    )
    parser.add_argument(
        "--n_obs_stochastic", type=int, help="Number of the stochastic runs", required=True
    )
    parser.add_argument(
        "--deterministic_folder_name",
        type=str,
        help="Name of the folder with deterministic solution",
        required=True,
    )
    parser.add_argument(
        "--action",
        type=str,
        help="Type of action: [plot_time, animation_time, plot_diagram]",
        required=True
    )

    results = parser.parse_args()
    stochastic_folder = results.stochastic_folder_name
    n_obs = results.n_obs_stochastic
    deterministic_folder = results.deterministic_folder_name
    action_type = results.action

    if action_type == "plot_time":
        plot_results(stochastic_folder, deterministic_folder,
                     n_obs, savefig=False)
    elif action_type == "animation_time":
        animate_results(stochastic_folder, deterministic_folder, n_obs)
    elif action_type == "plot_diagram":
        plot_phase_space(stochastic_folder, deterministic_folder,
                         n_obs, savefig=False)
    else:
        print(f'{[action_type]} is not a valid action parameter')
