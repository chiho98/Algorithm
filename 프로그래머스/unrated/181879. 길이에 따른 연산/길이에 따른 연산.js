function solution(num_list) {
    if (num_list.length >= 11) {
        let sum = 0;
        for (let i = 0; i < num_list.length; i++) {
            sum += num_list[i];
        }
        return sum;
    } else {
        let product = 1;
        for (let i = 0; i < num_list.length; i++) {
            product *= num_list[i];
        }
        return product;
    }
}