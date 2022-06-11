/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minOperations = function(nums, x) {
    let leftP = 0;
    let rightP = nums.length - 1;
    step = 0;
    while(leftP < rightP) {
        let sum = nums[leftP] + nums[rightP];
        console.log({sum})
        if(sum == x) {
            return step;
        } else if(sum < x) {
            step++;
            leftP++;
        } else {
            step++;
            rightP--;
        }
    }
    return step;
};
let nums = [1,1,4,2,3], x = 5
console.log(minOperations(nums, 5))