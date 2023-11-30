use std::fs;

fn main() {
    let input_string = fs::read_to_string("input").expect("Should have been able to read the file");

    // split string into a list of strings by newline
    let trimmed_input_strings = input_string.split("\n").collect::<Vec<&str>>();

    // trim the strings
    let input_strings = trimmed_input_strings
        .iter()
        .map(|x| x.trim())
        .collect::<Vec<&str>>();

    // convert list of strings to list of ints
    let input_ints = input_strings
        .iter()
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();

    // Sum the ints
    let mut sum = 0;
    let mut seen = Vec::new();
    let mut break_out = false;
    while !break_out {
        for freq in input_ints.iter() {
            if seen.contains(&sum) {
                println!("{} has been seen before", sum);
                break_out = true;
                break;
            }
            seen.push(sum);
            sum += freq;
        }
    }
}
