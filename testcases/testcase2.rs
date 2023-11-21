fn main()
{
    static mut a:bool=true;
    let mut i:i32=0;
    while !a 
    {
        i*=i+2;
    }
    let mut array:[i32;10];
    let mut index:i32=0;
    let mut value:i64=0;
    for (index,value) in (0..=5).enumerate()
    {
        index+=index;
        value+=value;
    }
}