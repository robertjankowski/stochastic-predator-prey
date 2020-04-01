pub struct Parameters {
    t_start: f64,
    t_end: f64,
    length: usize,
}

impl Parameters {
    pub fn new(t_start: f64, t_end: f64, length: usize) -> Parameters {
        Parameters {
            t_start,
            t_end,
            length,
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
}
