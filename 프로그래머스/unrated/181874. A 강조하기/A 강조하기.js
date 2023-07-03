function solution(myString) {
    var answer = '';
    for (let i = 0; i < myString.length; i++) {
        if (myString[i] === "a" || myString[i] === "A") {
            answer += myString[i].toUpperCase();
        } 
        else {
            answer += myString[i].toLowerCase();
        }
    }
    console.log(answer);
    return answer;
}