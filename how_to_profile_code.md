## How to profile Rust code

1. `cargo build --release`
2. `perf record --call-graph dwarf ./target/release/stochastic-predator-prey`
3. `perf report`
