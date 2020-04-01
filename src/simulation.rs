use itertools_num::linspace;

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
    dt: f64
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

    pub fn t_start(&self) -> f64 {
        self.t_start
    }

    pub fn t_end(&self) -> f64 {
        self.t_end
    }

    pub fn length(&self) -> usize {
        self.length
    }

    pub fn dt(&self) -> f64 {
        self.dt
    }

    pub fn get_time(&self) -> Vec<f64> {
        let time = linspace::<f64>(self.t_start, self.t_end, self.length);
        time.collect::<Vec<_>>()
    }
}
