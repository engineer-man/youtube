#![allow(dead_code,unused_variables)]

// make structs
struct Data {
    num1: i32,
    num2: i32,
    str1: String,
    optional_num: Option<i32>
}

struct TwoNums(i32, i32);

struct Calculator;

// implement methods on a struct
impl Data {
    fn new() -> Self {
        Data {
            num1: 2,
            num2: 4,
            str1: "some string".to_string(),
            optional_num: Some(8)
        }
    }

    fn sum(&self) -> i32 {
        self.num1 + self.num2
    }
}

// make a trait
trait Transform {
    fn rev(&self) -> String;

    fn output_rev(&self) {
        println!("{}", self.rev());
    }
}

impl Transform for Data {
    fn rev(&self) -> String {
        self.str1.chars().rev().collect::<String>()
    }
}

// implement methods on a unit struct
impl Calculator {
    fn add(n1: i32, n2: i32) -> i32 {
        n1 + n2
    }
    fn sub(n1: i32, n2: i32) -> i32 {
        n1 - n2
    }
    fn mul(n1: i32, n2: i32) -> i32 {
        n1 * n2
    }
    fn div(n1: i32, n2: i32) -> f32 {
        (n1 / n2) as f32
    }
}

fn main() {
    let a = Data{
        num1: 4,
        num2: 3,
        str1: "whatever".to_string(),
        optional_num: None
    };
    println!("{}", a.sum());

    let b = Data{ num1: 8, ..a };
    println!("{}", b.sum());

    let mut c = Data::new();
    c.num1 = 3;
    println!("{}", c.sum());
    println!("{}", c.rev());
    c.output_rev();

    let d = TwoNums(4, 3);
    println!("{}, {}", d.0, d.1);

    println!("{}", Calculator::add(3, 2));
    println!("{}", Calculator::sub(3, 2));
    println!("{}", Calculator::mul(3, 2));
    println!("{}", Calculator::div(3, 2));
}
