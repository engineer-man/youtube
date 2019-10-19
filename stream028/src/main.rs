use std::io::{stdin, stdout, Write};
use std::fs;
use rand::Rng;

struct Leader {
    name: String,
    score: u8
}

fn write_scores(leaders: Vec<Leader>) {
    let mut contents = String::new();

    for leader in leaders {
        contents.push_str(&leader.name);
        contents.push('|');
        contents.push_str(&leader.score.to_string());
        contents.push('\n');
    }

    fs::write("scores.txt", contents)
        .expect("failed to write file");
}

fn main() {
    let mut leaders: Vec<Leader> = Vec::new();
    let mut name = String::new();

    match fs::read_to_string("scores.txt") {
        Ok(contents) => {
            let contents = contents.trim();

            if contents != "" {
                for line in contents.split('\n') {
                    let pieces: Vec<&str> = line.split('|').collect();

                    leaders.push(Leader {
                        name: pieces[0].to_string(),
                        score: pieces[1].parse().unwrap()
                    });
                }
            }
        },
        Err(_) => {}
    }

    if leaders.len() == 0 {
        println!("no high score data yet!\n");
    } else {
        println!("high scores:");

        for leader in &leaders {
            println!("  {}: {}", leader.name, leader.score);
        }
    }

    loop {
        print!("what is your name? ");

        stdout().flush()
            .expect("failed to flush");

        stdin().read_line(&mut name)
            .expect("failed to read");

        name = name.trim().to_string();

        if name != "" {
            break
        }
    }

    println!("welcome, {}", name.trim());

    let mut rng = rand::thread_rng();

    println!("i'll be guessing numbers between 1 and 50");
    println!("you must guess if my next guess is higher or lower");
    println!("good luck!\n");

    let mut guess: u8 = rng.gen_range(1, 51);
    let mut next_guess: u8;

    let mut score = 0;

    loop {
        let mut user_guess = String::new();

        println!("my guess: {}", guess);
        print!("high or lower? [h/l]: ");

        stdout().flush()
            .expect("failed to flush");

        stdin().read_line(&mut user_guess)
            .expect("failed to read");

        user_guess = user_guess.trim().to_string();

        loop {
            next_guess = rng.gen_range(1, 51);
            if guess == next_guess {
                continue
            } else {
                break
            }
        }

        if user_guess == "h" && next_guess > guess {
            println!("you got it right, next round");

            score += 1;
            guess = next_guess;
        } else if user_guess == "l" && next_guess < guess {
            println!("you got it right, next round");

            score += 1;
            guess = next_guess;
        } else {
            println!("sorry, you lose, the number was: {}", next_guess);
            break;
        }
    }

    let mut exists = false;

    for leader in &mut leaders {
        if leader.name == name {
            if score > leader.score {
                leader.score = score;
            }
            exists = true;
        }
    }

    if !exists {
        leaders.push(Leader { name, score });
    }

    write_scores(leaders);

    println!("thanks for playing!");
}
