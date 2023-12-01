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
    let input_string = fs::read_to_string("input").expect("Should have been able to read the file");

    // split string into a list of strings by newline
    let trimmed_input_strings = input_string.split("\n").collect::<Vec<&str>>();

    // trim the strings
    let input_strings = trimmed_input_strings
        .iter()
        .map(|x| x.trim())
        .collect::<Vec<&str>>();
}

fn part2() {
    println!("Running Part 2:")
}
