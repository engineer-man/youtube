#[allow(dead_code,unused_variables)]
fn main() {
    let age = 25;

    // if
    if age > 21 {
        println!("over 21");
    } else if age < 21 {
        println!("under 21");
    } else {
        println!("exactly 21");
    }

    // if with output capture
    let old_enough = if age > 21 {
        true
    } else {
        false
    };

    // compressed version, closest to ternary as is possible
    let old_enough = if age > 21 { true } else { false };

    // match statement (used like a switch)
    match age {
        21 => println!("age is 21"),
        22 => println!("age is 22"),
        23 | 24 => println!("age is 23 or 24"),
        25..=28 => println!("age is between 25 and 28"),
        n if n < 5 => println!("age is less than 5"),
        n if n > 50 => println!("age is greater than 50"),
        _ => println!("age is something else")
    }

    // infinite loop
    let mut i = 0;
    let x = loop {
        if i == 10 {
            break i;
        }
        i += 1;
    };

    // while
    let mut j = 0;
    while j < 10 {
        j += 1;
    }

    // for loop - for (i = 0; i < 10; ++i)
    for i in 0..10 {
        println!("{}", i);
    }

    // iterations
    let nums = vec![1, 2, 3, 4, 5];
    for num in nums {
        println!("{}", num);
    }
}
