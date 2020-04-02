use gnuplot::*;
use itertools_num::linspace;
use rand_distr::{Distribution, Normal};

mod simulation;
use simulation::{LotkaVolterraParameters, SimulationParameters, LotkaVolterraSimulation};

fn generate_from_normal_distr(mu: f64, std: f64) -> f64 {
    let normal_distr = Normal::new(mu, std).unwrap();
    normal_distr.sample(&mut rand::thread_rng())
}

fn ornstein_uhlenbeck_process() {
    // Example Ornstein-Uhlenbeck process
    // https://www.pik-potsdam.de/members/franke/lecture-sose-2016/introduction-to-python.pdf
    let t0 = 0.0;
    let t_end = 2.0;
    let length = 2000;
    let parameters = SimulationParameters::new(0.0, 2.0, 1000);
    let theta = 1.3;
    let mu = 1.8;
    let sigma = 0.4;

    let t = linspace::<f64>(
        parameters.t_start(),
        parameters.t_end(),
        parameters.length(),
    );
    let dt = (t_end - t0) / length as f64;

    let mut y: Vec<f64> = vec![0.0; length];
    let mut y0: Vec<_> = (0..length)
        .map(|_| generate_from_normal_distr(0.0, 1.0))
        .collect();

    let drift = |y: f64, t: f64| theta * (mu - y);
    let diffusion = |y: f64, t: f64| sigma;
    let noise: Vec<_> = (0..length)
        .map(|_| generate_from_normal_distr(0.0, 1.0) * dt.sqrt())
        .collect();

    for i in 1..length {
        y[i] = y[i - 1]
            + drift(y[i - 1], i as f64 * dt) * dt
            + diffusion(y[i - 1], i as f64 * dt) * noise[i];
    }
    let x: Vec<_> = (0..length).collect();

    let mut fg = Figure::new();
    fg.axes2d()
        .set_title("Ornstein-Uhlenbeck process", &[])
        .set_legend(Graph(0.5), Graph(0.9), &[], &[])
        .set_x_label("t", &[])
        .set_y_label("y", &[])
        .lines(x, y, &[Caption("First")]);
    fg.show().unwrap();
}

fn lotka_voterra() {
    let lvp = LotkaVolterraParameters::new(0.6, 0.1, 0.75, 1.5);
    let sp = SimulationParameters::new(0.0, 20.0, 1000);
    let mut lv_simulation = LotkaVolterraSimulation::new(&sp, lvp);
    lv_simulation.run_single_deterministic(5.0, 1.0);
    lv_simulation.run_single_deterministic(5.0, 3.0);
    lv_simulation.run_single_deterministic(5.0, 5.0);
    lv_simulation.run_single_deterministic(5.0, 10.0);
    lv_simulation.run_single_deterministic(5.0, 20.0);
    
    // lv_simulation.plot_prey_predators(None);
    lv_simulation.save_data(Some("test.csv"));
}

fn plot_prey_predators(x: &Vec<f64>, y: &Vec<f64>, time: &Vec<f64>, filename: Option<&str>) {
    let mut fg = Figure::new();
    fg.axes2d()
        .set_title("Deterministic Lotka-Volterra Equations", &[])
        .set_legend(Graph(0.5), Graph(0.9), &[], &[])
        .set_x_label("t", &[])
        .set_y_label("population", &[])
        .lines(time, x, &[Caption("Prey")])
        .lines(time, y, &[Caption("Predator")]);
    filename.map(|s| fg.set_terminal("pdfcairo", s));
    fg.show().unwrap();
}

fn main() {
    lotka_voterra();
}
