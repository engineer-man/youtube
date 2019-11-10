use std::io::{stdin, stdout, Write};

fn read(input: &mut String) {
    stdout().flush()
        .expect("failed to flush");
    stdin().read_line(input)
        .expect("failed to read");
}

fn main() {
    println!("welcome to engineer man's calculator!");
    println!("---------");

    loop {
        let mut num1 = String::new();
        let mut num2 = String::new();
        let mut operator = String::new();

        print!("what is the first number?: ");
        read(&mut num1);

        print!("what is the second number?: ");
        read(&mut num2);

        print!("what operation would you like to do? [+-*/]: ");
        read(&mut operator);

        let num1: f32 = num1.trim().parse().unwrap();
        let num2: f32 = num2.trim().parse().unwrap();
        let operator: char = operator.trim().chars().next().unwrap();

        let operators = String::from("+-*/");

        if !operators.contains(operator) {
            println!("unknown operator");
            continue;
        }

        let result = match operator {
            '+' => num1 + num2,
            '-' => num1 - num2,
            '*' => num1 * num2,
            '/' => num1 / num2,
            _ => panic!("error in operator")
        };

        println!("the result of {} {} {} = {}", num1, operator, num2, result);
    }
}
