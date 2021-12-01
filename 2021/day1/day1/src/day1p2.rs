use std::fs::File;
use std::io::{BufReader, BufRead};

const FNAME: &str = "../../input.txt";
fn main() {
    let f = File::open(FNAME).expect("Unable to open data file");
    let reader = BufReader::new(f);
    let vec: Vec<String> = reader
        .lines()
        .collect::<Result<_, _>>()
        .unwrap();
    let nums: Vec<i32> = vec.into_iter()
        .map(|x| x.parse::<i32>()
        .unwrap())
        .collect();

    let mut totals = 0;
    let mut n1 = nums[0];
    let mut n2 = nums[1];
    let mut n3 = nums[2];
    for i in 3..nums.len() {
        if (n1+n2+n3) < (n2+n3+nums[i]) {
            totals += 1
        }
        n1 = n2;
        n2 = n3;
        n3 = nums[i];
    }
    println!("{}", totals);
}