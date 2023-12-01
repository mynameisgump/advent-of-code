use std::env;

fn main() {
    let args: Vec<_> = env::args().collect();
    if args.len() > 1 {
        if args[1] == "1" {
            part1();
        } else if args[1] == "2" {
            part2();
        } else {
            println!("Invalid argument");
        }
    }
}

fn part1() {
    println!("Running Part 1:")
}

fn part2() {
    println!("Running Part 2:")
}
