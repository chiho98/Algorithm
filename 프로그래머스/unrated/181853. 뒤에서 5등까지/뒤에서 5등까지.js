function solution(num_list) {
    const arr = num_list.sort((a,b) => a - b)
    const answer = []
    for(let i = 0 ; i <= 4; i++) {
        answer.push(num_list[i])
    }
    return answer
}