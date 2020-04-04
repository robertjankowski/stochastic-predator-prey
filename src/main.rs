mod simulation;
use simulation::{LotkaVolterraParameters, LotkaVolterraSimulation, SimulationParameters};

fn main() {
    let lvp = LotkaVolterraParameters::new(0.6, 0.2, 0.75, 1.2);
    let sp = SimulationParameters::new(0.0, 15.0, 1000000);
    let mut lv_simulation = LotkaVolterraSimulation::new(&sp, lvp);
    let n_iteration = 10;
    let initial_x = 3.0;
    let initial_y = 5.0;
    let sigma_x = 0.1;
    let sigma_y = 0.2;
    lv_simulation.run_stochastic(n_iteration, initial_x, initial_y, sigma_x, sigma_y);
    //lv_simulation.save_data("stochastic1");
}
