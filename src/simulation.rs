use itertools_num::linspace;
use std::fs;
use std::io::Write;

type PredatorsPreys = (Vec<f64>, Vec<f64>);

pub struct LotkaVolterraSimulation {
    predators_preys: Vec<PredatorsPreys>,
    time: Vec<f64>,
    dt: f64,
    lvp: LotkaVolterraParameters,
}

impl LotkaVolterraSimulation {
    pub fn new(sp: &SimulationParameters, lvp: LotkaVolterraParameters) -> LotkaVolterraSimulation {
        LotkaVolterraSimulation {
            predators_preys: vec![],
            time: sp.get_time(),
            dt: sp.dt(),
            lvp,
        }
    }

    fn get_initial_predators_preys(
        &self,
        length: usize,
        initial_x: f64,
        initial_y: f64,
    ) -> (Vec<f64>, Vec<f64>) {
        let mut x = vec![0.0; length];
        let mut y = vec![0.0; length];
        x[0] = initial_x;
        y[0] = initial_y;
        (x, y)
    }

    pub fn save_data(&self, folder: &str) {
        fs::create_dir(format!("data/{}", folder)).expect("Unable to create folder.");
        let lv_params = format!(
            "dt={}_alpha={}_beta={}_delta={}_gamma={}",
            self.dt,
            self.lvp.alpha(),
            self.lvp.beta(),
            self.lvp.delta(),
            self.lvp.gamma()
        );

        let values: Vec<_> = self
            .predators_preys
            .iter()
            .map(|(xs, ys)| {
                let xy: Vec<(f64, f64)> = xs.iter().map(|x| x.clone()).zip(ys.clone()).collect();
                xy
            })
            .collect();
        let mut i = 0;
        for vec in &values {
            let filename = format!("data/{}/{}_i={}.csv", folder, lv_params, i);
            fs::File::create(filename)
                .map(|mut f| {
                    for (x, y) in vec {
                        write!(f, "{:.4},{:.4}\n", x, y);
                    }
                })
                .expect("Unable to create file.");
            i += 1;
        }
    }

    pub fn run_single_deterministic(&mut self, initial_x: f64, initial_y: f64) {
        let (mut x, mut y) =
            self.get_initial_predators_preys(self.time.len(), initial_x, initial_y);

        for i in 1..self.time.len() {
            x[i] = x[i - 1]
                + (self.lvp.alpha() * x[i - 1] - self.lvp.beta() * x[i - 1] * y[i - 1]) * self.dt;
            y[i] = y[i - 1]
                + (self.lvp.delta() * x[i - 1] * y[i - 1] - self.lvp.gamma() * y[i - 1]) * self.dt;
        }
        self.predators_preys.push((x, y));
    }

    pub fn run_deterministic(&mut self, n_iteration: i32, initial_x: f64, initial_y: f64) {
        for _ in 0..n_iteration {
            self.run_single_deterministic(initial_x, initial_y);
        }
    }
}

pub struct LotkaVolterraParameters {
    alpha: f64, // the natural growing rate of rabbits, when there's no fox
    beta: f64,  // the natural dying rate of rabbits, due to predation
    delta: f64, // the natural dying rate of fox, when there's no rabbit
    gamma: f64, // the factor describing how many caught rabbits let create a new fox
}

impl LotkaVolterraParameters {
    pub fn new(alpha: f64, beta: f64, delta: f64, gamma: f64) -> LotkaVolterraParameters {
        LotkaVolterraParameters {
            alpha,
            beta,
            delta,
            gamma,
        }
    }

    pub fn alpha(&self) -> f64 {
        self.alpha
    }

    pub fn beta(&self) -> f64 {
        self.beta
    }

    pub fn delta(&self) -> f64 {
        self.delta
    }
    pub fn gamma(&self) -> f64 {
        self.gamma
    }
}

pub struct SimulationParameters {
    t_start: f64,
    t_end: f64,
    length: usize,
    dt: f64,
}

impl SimulationParameters {
    pub fn new(t_start: f64, t_end: f64, length: usize) -> SimulationParameters {
        let dt = (t_end - t_start) / length as f64;
        SimulationParameters {
            t_start,
            t_end,
            length,
            dt,
        }
    }

    pub fn dt(&self) -> f64 {
        self.dt
    }

    pub fn get_time(&self) -> Vec<f64> {
        let time = linspace::<f64>(self.t_start, self.t_end, self.length);
        time.collect::<Vec<_>>()
    }
}
