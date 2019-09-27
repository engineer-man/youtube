fn main() {
    // define simple enum
    enum Color {
        Red,
        Green,
        Blue,
        Orange,
        Custom(String), // tuple struct style
        Coord{ x: i32, y: i32 } // classic struct style
    }

    // explicit values
    enum Number {
        One = 1,
        Five = 5,
        Ten = 0xA
    }

    println!("{}", Number::One as i32);
    println!("{}", Number::Five as i32);
    println!("{}", Number::Ten as i32);

    let favorite: Color = Color::Green;
    let custom: Color = Color::Custom("pink".to_string());

    // check with if let
    if let Color::Green = favorite {
        println!("favorite color is green");
    }

    // check with match
    match favorite {
        Color::Green => println!("favorite color is green"),
        Color::Blue => println!("favorite color is blue"),
        _ => {}
    }

    match custom {
        Color::Custom(color) => println!("custom color: {}", color),
        _ => {}
    }

    // built-in Option<T> enum
    let mut age: Option<i32> = None;
    age = Some(18);

    match age {
        Some(age) => {
            if age >= 21 {
                println!("can have beer");
            } else {
                println!("can't have beer, only {}", age);
            }
        },
        None => println!("unknown age")
    }
}
