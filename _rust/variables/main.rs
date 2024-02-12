// 2024-02-12
// Varibles in Rust 

fn main() {

    // --- Int variables ---

    // Ex. 1 
    // variables type annotated first
    let x: i32;              // `i32` -> 32-bit integer type
    x = 42;
    println!("{}", x); 

    // Ex. 2
    // variables type annotated using one line
    let x: i32 = 21;                             
    println!("{}", x);

    // --- float variables ---
    // Ex. 1 
    let y: f32;              // `f32` -> 32-bit float type
    y = 42.24;
    println!("{}", y);

    // Ex. 2
    let y: f32 = 21.12;
    println!("{}", y);

    // --- string variables ---
    
    // Ex.1
    let string = "To jest przykładowy string przypisany do zmiennej w jęzuku Rust";
    println!("{}", string);

    // `for` loop exapmle
    for i in string.chars() {
        println!("{}", i);
    }

    // ---------------------
}