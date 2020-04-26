### Simulation of stochastic Lotka-Volterra model


[Deterministic Lotka-Volterra model](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) has form:

$$
\frac{dx}{dt} = \alpha x - \beta xy
$$
$$
\frac{dy}{dt} = \delta xy - \gamma y
$$

Where `x` - number of prey, `y` number of predator.

Adding to the equations the stochastic component:

$$
dx = (\alpha x - \beta xy) dt + \sigma_1 dW 
$$
$$
dy = (\delta xy - \gamma y) dt + \sigma_2 dW
$$

We can solve those equations using numerical approach i.e. Euler-Maruyama method

$$
x_t = x_{t-1} + (\alpha x_{t-1} - \beta x_{t-1}y_{t-1}) \Delta t + \sigma_1 \Delta W 
$$
$$
y_t = y_{t-1} + (\delta x_{t-1}y_{t-1} - \gamma y_{t-1}) \Delta t + \sigma_2 \Delta W
$$

Where $\Delta W$ is Wiener process ($\mathcal{N}(0, \Delta t)$), $\sigma_1$ and $\sigma_2$ are constants.

### Results for: $\alpha = 1.5, \beta=1, \delta=1, \gamma=3$ with $\sigma_x \in \{ 0.1, 0.5\}$ and $\sigma_y \in \{ 0.1, 0.5\}$

| ![a1](figures/animation_alpha=1.5_beta=1_delta=1_gamma=3_sigma_x=0.1_sigma_y=0.1.gif) | ![a2](figures/animation_alpha=1.5_beta=1_delta=1_gamma=3_sigma_x=0.1_sigma_y=0.5.gif) |
| :-----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------: |
| ![a3](figures/animation_alpha=1.5_beta=1_delta=1_gamma=3_sigma_x=0.5_sigma_y=0.1.gif) | ![a4](figures/animation_alpha=1.5_beta=1_delta=1_gamma=3_sigma_x=0.5_sigma_y=0.5.gif) |

### Results for: $\alpha = 0.9, \beta=0.5, \delta=0.25, \gamma=0.75$ with $\sigma_x \in \{ 0.1, 0.5\}$ and $\sigma_y \in \{ 0.1, 0.5\}$

| ![a1](figures/animation_alpha=0.9_beta=0.5_delta=0.25_gamma=0.75_sigma_x=0.1_sigma_y=0.1.gif) | ![a2](figures/animation_alpha=0.9_beta=0.5_delta=0.25_gamma=0.75_sigma_x=0.1_sigma_y=0.5.gif) |
| :-------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------: |
| ![a3](figures/animation_alpha=0.9_beta=0.5_delta=0.25_gamma=0.75_sigma_x=0.5_sigma_y=0.1.gif) | ![a4](figures/animation_alpha=0.9_beta=0.5_delta=0.25_gamma=0.75_sigma_x=0.5_sigma_y=0.5.gif) |