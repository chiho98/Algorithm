function solution(num_list) {
    var answer = [];
    for(let i = 0; i < num_list.length; i++) {
        answer.push(num_list[i]);
    }
    const num1 = num_list.length - 1;
    const num2 = num_list.length - 2;
    if(num_list[num1] > num_list[num2]) {
        answer.push(num_list[num1] - num_list[num2]);
    } else {
        answer.push(num_list[num1] * 2);
    }
    return answer;
}