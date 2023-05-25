function solution(numbers, num1, num2) {
    // return numbers.slice(num1, num2+1);
    const answer = [];
    for (let i = num1; i <= num2; i++) {
        answer.push(numbers[i])
    }
    return answer;
}