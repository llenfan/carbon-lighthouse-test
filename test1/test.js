function solution(arr) {

  let pos = 1;
  let max = arr[0];
  let winterMax = arr[0]; 

  for(let i = 1; i < arr.length; i++) {
    // Iterate the array and check if the current element is lower than my current max
    if (arr[i] < winterMax) {
      // Set as possible solution all the numbers that are below my current max
      pos = i+1;
      // Assign a new max in case there has been a number bigger than my winter max and that is not part of the summer
      winterMax = max;
    } else if (arr[i] > max) {
      // Set a new max if the current element is bigger than all the numbers till now.
      max = arr[i];
    }
  }
  return pos;
}