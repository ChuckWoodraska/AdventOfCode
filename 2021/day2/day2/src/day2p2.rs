use std::fs::File;
use std::io::{BufReader, BufRead};

struct Instruction {
    direction: String,
    depth: i32
}

const FNAME: &str = "../../input.txt";
fn main() {
    let f = File::open(FNAME).expect("Unable to open data file");
    let reader = BufReader::new(f);
    let vec: Vec<String> = reader
        .lines()
        .collect::<Result<_, _>>()
        .unwrap();


    let instructions: Vec<Instruction> = vec.into_iter()
        .map(|x| {
            let (direction, depth) = x
                .split_once(' ')
                .unwrap();

            Instruction {
                direction: direction.to_string(),
                depth: depth.parse().unwrap(),
            }
        })
        .collect();

    let mut h = 0;
    let mut d = 0;
    let mut a = 0;
    for i in instructions {
        match i.direction.as_str() {
            "down" => a += i.depth,
            "up" => a -= i.depth,
            "forward" => {
                h += i.depth;
                d += a*i.depth;
            }
            _ => println!("something else!"),
        }
    }
    println!("{}", h*d);
}