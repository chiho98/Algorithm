function solution(arr1, arr2) {
    const length1 = arr1.length;
    const length2 = arr2.length;
    let a = 0;
    let b = 0;
    
    if(length1 > length2) {
        return 1
    } else if(length1 < length2) {
        return -1
    } else if(length1 === length2) {
        for(let i = 0; i < length1; i++) {
            a += arr1[i]
            b += arr2[i]
        }
    }
    if(a > b) {
        return 1
    } else if(a < b) {
        return -1
    } else {
        return 0
    }
}