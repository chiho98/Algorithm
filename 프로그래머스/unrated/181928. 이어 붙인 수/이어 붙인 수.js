function solution(num_list) {
    let answer1 = 0;
    let answer2 = 0;
    for(let i = 0; i < num_list.length; i++) {
        if(num_list[i] % 2 === 0) {
            answer1 += num_list[i].toString();
        } else if(num_list[i] % 2 === 1) {
            answer2 += num_list[i].toString();
        }
    }
    return parseInt(answer1) + parseInt(answer2);
}