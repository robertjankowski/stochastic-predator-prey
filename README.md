### Simulation of Lotka-Volterra model with stochastic component


[Deterministic Lotka-Volterra model](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations) has form:

<p align="center"><img src="/tex/2b8a60510c7bcaa616c51f53092b56d8.svg?invert_in_darkmode&sanitize=true" align=middle width=217.3180515pt height=33.81208709999999pt/></p>

Where `x` - number of prey, `y` number of predator.

Adding to the equations the stochastic component:

<p align="center"><img src="/tex/a23aa85317f49822431276122419c907.svg?invert_in_darkmode&sanitize=true" align=middle width=392.40126255pt height=16.438356pt/></p>

We can solve this equations using numerical approach (Euler-Maruyama method)

<p align="center"><img src="/tex/b0c5a76fbdb7bbc5e35838fd1a2974d3.svg?invert_in_darkmode&sanitize=true" align=middle width=643.6270665pt height=16.438356pt/></p>

Where <img src="/tex/8d9b176fd459e329c57782488a188936.svg?invert_in_darkmode&sanitize=true" align=middle width=31.50693314999999pt height=22.465723500000017pt/> is Wiener process (<img src="/tex/9d1ddb149d5ffa2d775cf7abfa2a4ed3.svg?invert_in_darkmode&sanitize=true" align=middle width=63.855150149999986pt height=24.65753399999998pt/>), <img src="/tex/9811b1e861c58c0f72de45f573e7eea4.svg?invert_in_darkmode&sanitize=true" align=middle width=15.94565279999999pt height=14.15524440000002pt/> and <img src="/tex/0318cc8a44e98dfa8db4cd5b6f731ed4.svg?invert_in_darkmode&sanitize=true" align=middle width=15.94565279999999pt height=14.15524440000002pt/> are constants.
