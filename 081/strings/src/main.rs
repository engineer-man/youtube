fn main() {
    // immutable literal stored in read-only data
    let name1: &'static str = "engineer man";
    println!("{}", name1);

    // create mutable growable string on heap
    let mut name2: String = String::new();
    name2 = name2 + "engineer";
    name2.push_str(" man");
    println!("{}", name2);

    // string slices
    let name3: &str = &name1[..8];
    let name4: &str = &name1[9..];
    println!("{} {}", name3, name4);

    // loop over characters
    for c in name2.chars() {
        print!("{} ", c);
    }
    println!("");
}
