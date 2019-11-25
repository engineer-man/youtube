#![allow(dead_code,unused_variables)]

use std::collections::HashMap;

fn main() {
    // initialization
    let nums: Vec<i32> = Vec::new();
    let mut nums = vec![1, 2, 3];

    // insert values
    nums.push(4);
    nums.push(5);
    nums.push(6);

    // access specific element(s)
    &nums[2];
    &nums[2..];
    nums.get(2);

    // remove elements
    nums.remove(2);

    // iterating over values
    for num in &nums {
        println!("{}", num);
    }

    // modifying values in place
    for num in &mut nums {
        *num += 1;
    }

    // random types in vectors
    enum Value {
        Int(i32),
        Float(f32)
    };

    let random = vec![Value::Int(3), Value::Float(3.3)];

    // initialization
    let mut numbers: HashMap<&str, i32> = HashMap::new();

    // insert/update values
    numbers.insert("one", 1);
    numbers.insert("two", 2);
    numbers.insert("three", 3);

    // access values
    println!("{}", numbers.get("two").unwrap());

    if numbers.contains_key("two") {
        println!("{}", numbers.get("two").unwrap());
    }

    match numbers.get("two") {
        Some(val) => println!("{}", val),
        None => println!("key does not exist")
    };

    // remove value
    numbers.remove("three");

    // iterate over values
    for (key, value) in &numbers {
        println!("{} => {}", key, value);
    }
}
