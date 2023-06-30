function solution(my_string, is_prefix) {
    let a = ""
    let b = ""
    
    for(let i = 0; i < is_prefix.length; i++) {
        a += is_prefix[i]
        b += my_string[i]
    } 
    if (a === b) {
        return 1
    } else {
        return 0
    }
}