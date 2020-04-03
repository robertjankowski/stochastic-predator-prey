use rand_distr::{Distribution, Normal};

mod simulation;
use simulation::{LotkaVolterraParameters, LotkaVolterraSimulation, SimulationParameters};

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
    let theta = 1.3;
    let mu = 1.8;
    let sigma = 0.4;

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
}

fn main() {
    let lvp = LotkaVolterraParameters::new(0.6, 0.1, 0.75, 1.5);
    let sp = SimulationParameters::new(0.0, 20.0, 10000);
    let mut lv_simulation = LotkaVolterraSimulation::new(&sp, lvp);
    lv_simulation.run_deterministic(20, 1.0, 4.0);
    lv_simulation.save_data("deterministic2");
}
