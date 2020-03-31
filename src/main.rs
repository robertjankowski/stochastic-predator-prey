use rand_distr::{Distribution, Normal};

fn main() {
    let sigma = 1.4;
    let normal = Normal::new(0.0, sigma).unwrap();
    let v = normal.sample(&mut rand::thread_rng());
    println!("{} is generated from N(0, {})", v, sigma);
}
