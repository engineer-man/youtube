fn main() {
    let name = String::from("engineer man");

    let size = get_length(&name);
    println!("{} is {} characters", name, size);

    borrow_name(&name);

    println!("{}", name);

    println!("{}", add(1, 2));
    println!("{}", add(1, 8));

    let mut num = 1;
    inc(&mut num);
}

fn inc(n1: &mut i32) {
    *n1 = *n1 + 1;
}

fn get_length(s: &str) -> usize {
    s.chars().count()
}

fn borrow_name(s: &String) {
    print!("{}", s);
}

fn add(n1: i32, n2: i32) -> i32 {
    n1 + n2
}
