function solution(myString, pat) {
    var answer = 0;
    for (let i = 0; i < myString.length; i++) {
        if(myString[i] === "A") {
            answer += "B"
        } else {
            answer += "A"
        }
    }
    if(answer.includes(pat)) {
        return 1
    } return 0
    return answer;
}