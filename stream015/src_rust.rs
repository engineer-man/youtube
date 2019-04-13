use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let start_num = &args[1].parse::<i32>().unwrap();
    let count = &args[2].parse::<i32>().unwrap();

    let mut list: Vec<i32> = Vec::new();

    for i in 0..*count {
        list.push(i * start_num);
    }

    let mut sum = 0;
    let mut divisible = 0;

    for i in 0..list.len() {
        sum += list[i];
        if list[i] % 10 == 0 {
            divisible += 1;
        }
    }

    println!("{} {}", sum, divisible);
}
