mod simulation;
use simulation::{LotkaVolterraParameters, LotkaVolterraSimulation, SimulationParameters};

fn main() {
    let lvp = LotkaVolterraParameters::new(0.9, 0.5, 0.25, 0.75);
    let sp = SimulationParameters::new(0.0, 30.0, 2000);
    let sigma_x = 0.5;
    let sigma_y = 0.1;
    let mut lv_simulation = LotkaVolterraSimulation::new(&sp, lvp, sigma_x, sigma_y);
    let n_iteration = 10;
    let initial_x = 0.2;
    let initial_y = 0.5;
    lv_simulation.run_stochastic(n_iteration, initial_x, initial_y);
    // lv_simulation.run_deterministic(n_iteration, initial_x, initial_y);
    let stochastic_filename = format!(
        "stochastic_x={}_y={}_sigma-x={}_sigma-y={}",
        initial_x, initial_y, sigma_x, sigma_y
    );
    // let deterministic_filename = format!("deterministic_x={}_y={}", initial_x, initial_y);
    lv_simulation.save_data(&stochastic_filename);
}
