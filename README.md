### Simulation of stochastic Lotka-Volterra model


[Deterministic Lotka-Volterra model](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) has form:

<p align="center"><img src="/tex/af82ad02a586b9c256772f1103191a4d.svg?invert_in_darkmode&sanitize=true" align=middle width=110.1135585pt height=33.81208709999999pt/></p>
<p align="center"><img src="/tex/8b6426f8d05bf1c579313d8122a7d637.svg?invert_in_darkmode&sanitize=true" align=middle width=105.23191304999999pt height=33.81208709999999pt/></p>

Where `x` - number of prey, `y` number of predator.

Adding to the equations the stochastic component:

<p align="center"><img src="/tex/65ed167a9177e6314439e1081d18b83e.svg?invert_in_darkmode&sanitize=true" align=middle width=198.64146225pt height=16.438356pt/></p>
<p align="center"><img src="/tex/31788acdba84502dd0312131f43bcf26.svg?invert_in_darkmode&sanitize=true" align=middle width=193.75980195pt height=16.438356pt/></p>

We can solve those equations using numerical approach i.e. Euler-Maruyama method

<p align="center"><img src="/tex/0f5e7e77d5ff3be7d3e89b5dc6592558.svg?invert_in_darkmode&sanitize=true" align=middle width=325.51191915pt height=16.438356pt/></p>
<p align="center"><img src="/tex/e12a153cfe2eaf9e840a6657f6eb59f2.svg?invert_in_darkmode&sanitize=true" align=middle width=318.11515065000003pt height=16.438356pt/></p>

Where <img src="/tex/8d9b176fd459e329c57782488a188936.svg?invert_in_darkmode&sanitize=true" align=middle width=31.50693314999999pt height=22.465723500000017pt/> is Wiener process (<img src="/tex/9d1ddb149d5ffa2d775cf7abfa2a4ed3.svg?invert_in_darkmode&sanitize=true" align=middle width=63.855150149999986pt height=24.65753399999998pt/>), <img src="/tex/9811b1e861c58c0f72de45f573e7eea4.svg?invert_in_darkmode&sanitize=true" align=middle width=15.94565279999999pt height=14.15524440000002pt/> and <img src="/tex/0318cc8a44e98dfa8db4cd5b6f731ed4.svg?invert_in_darkmode&sanitize=true" align=middle width=15.94565279999999pt height=14.15524440000002pt/> are constants.

### Results for: <img src="/tex/2d015dbbba44c91dfeb84f2f01069795.svg?invert_in_darkmode&sanitize=true" align=middle width=193.34440619999998pt height=22.831056599999986pt/> with <img src="/tex/34277b7589d7c76b8871c5bf51945626.svg?invert_in_darkmode&sanitize=true" align=middle width=103.51409969999999pt height=24.65753399999998pt/> and <img src="/tex/a792d178d0107e0d0544e40b600b6c38.svg?invert_in_darkmode&sanitize=true" align=middle width=103.13933519999998pt height=24.65753399999998pt/>

| ![a1](figures/animation_alpha=1.5_beta=1_delta=1_gamma=3_sigma_x=0.1_sigma_y=0.1.gif) | ![a2](figures/animation_alpha=1.5_beta=1_delta=1_gamma=3_sigma_x=0.1_sigma_y=0.5.gif) |
| :-----------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------: |
| ![a3](figures/animation_alpha=1.5_beta=1_delta=1_gamma=3_sigma_x=0.5_sigma_y=0.1.gif) | ![a4](figures/animation_alpha=1.5_beta=1_delta=1_gamma=3_sigma_x=0.5_sigma_y=0.5.gif) |

### Results for: <img src="/tex/11ddf22ba37374c6b8f9ca1288149b61.svg?invert_in_darkmode&sanitize=true" align=middle width=248.13912584999994pt height=22.831056599999986pt/> with <img src="/tex/34277b7589d7c76b8871c5bf51945626.svg?invert_in_darkmode&sanitize=true" align=middle width=103.51409969999999pt height=24.65753399999998pt/> and <img src="/tex/a792d178d0107e0d0544e40b600b6c38.svg?invert_in_darkmode&sanitize=true" align=middle width=103.13933519999998pt height=24.65753399999998pt/>

| ![a1](figures/animation_alpha=0.9_beta=0.5_delta=0.25_gamma=0.75_sigma_x=0.1_sigma_y=0.1.gif) | ![a2](figures/animation_alpha=0.9_beta=0.5_delta=0.25_gamma=0.75_sigma_x=0.1_sigma_y=0.5.gif) |
| :-------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------: |
| ![a3](figures/animation_alpha=0.9_beta=0.5_delta=0.25_gamma=0.75_sigma_x=0.5_sigma_y=0.1.gif) | ![a4](figures/animation_alpha=0.9_beta=0.5_delta=0.25_gamma=0.75_sigma_x=0.5_sigma_y=0.5.gif) |