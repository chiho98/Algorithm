function solution(my_string, is_suffix) {
    const my_string2 = my_string.split("").reverse().join("");
    let a = ""
    let b = ""
    for (let i = 0; i < is_suffix.length; i++) {
        a += is_suffix[i]
        b += my_string2[i]
    }
    if (a === b.split("").reverse().join("")) {
        return 1
    }
    return 0
}