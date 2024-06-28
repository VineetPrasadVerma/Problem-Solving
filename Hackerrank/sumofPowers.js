// Input = 1 2 3 4
// output = (2*1) + (2*2) + (2*2*2) + (2*2*2*2) = 2 + 4 + 8 + 16 = 30

// find power of 2
const nums = [];
totalSum = 0
for (let i = 0; i < nums.length; i++) {
  power = 1
  counter = 0
  while (counter < nums[i]) {
    power *= 2
    counter += 1;
  }
  totalSum += power
}
console.log(totalSum)
