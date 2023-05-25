function solution(arr, k) {
    if (k % 2 === 1){
        return arr.map((arr) => arr*k);    
    }
    return arr.map((arr) => arr+k);
}