function solution(arr) {
    var answer = [];
    for(let i = 0; i < arr.length; i++) {
        const a = arr[i];
        for(let j = 0; j < a; j++) {
            answer.push(a);
        }
    }
    return answer;
}