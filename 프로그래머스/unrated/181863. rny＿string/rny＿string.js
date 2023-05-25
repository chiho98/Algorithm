function solution(rny_string) {
    var answer = '';
    const arr = rny_string.split("");
    for(let i = 0; i < arr.length; i++) {
        if (arr[i] === "m") {
            answer += "rn";
        } else {
            answer += arr[i];
        }
    }
    return answer;
}