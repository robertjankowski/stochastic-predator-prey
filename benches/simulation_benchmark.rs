#[path = "../src/simulation.rs"]
mod simulation;
use simulation::{LotkaVolterraParameters, LotkaVolterraSimulation, SimulationParameters};

use criterion::{criterion_group, criterion_main, Criterion};

pub fn criterion_benchmark(c: &mut Criterion) {
    c.bench_function("simulation benchmark", |b| {
        b.iter(|| {
            let lvp = LotkaVolterraParameters::new(0.6, 0.2, 0.75, 1.2);
            let sp = SimulationParameters::new(0.0, 15.0, 10000);
            let mut lv_simulation = LotkaVolterraSimulation::new(&sp, lvp);
            lv_simulation.run_single_stochastic(3.0, 5.0, 0.1, 0.2);
        })
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
