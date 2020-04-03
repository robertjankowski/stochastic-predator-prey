use rand_distr::{Distribution, Normal};

mod simulation;
use simulation::{LotkaVolterraParameters, LotkaVolterraSimulation, SimulationParameters};

fn main() {
    let lvp = LotkaVolterraParameters::new(0.6, 0.1, 0.75, 1.5);
    let sp = SimulationParameters::new(0.0, 20.0, 10000);
    let mut lv_simulation = LotkaVolterraSimulation::new(&sp, lvp);
    lv_simulation.run_stochastic(2, 4.0, 10.0, 0.2);
    lv_simulation.save_data("stochastic1");
}
