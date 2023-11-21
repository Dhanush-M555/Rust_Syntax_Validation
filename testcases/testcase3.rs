fn main() {
    static number:i32=10;
    let mut factorialwhile = 1;
    let mut counterwhile = factorialwhile;
    while counterwhile <= number {
        factorialwhile *= counterwhile;
        counterwhile += 1;
    }
    let mut factorialfor = 1;
    for counterfor in 1..=number {
        factorialfor *= counterfor;
    }

}