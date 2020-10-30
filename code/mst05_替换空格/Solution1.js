/**
 * @param {string} s
 * @return {string}
 */
var replaceSpace = function(s) {
  let resStr = '';
  for (let ch of s) {
    if (ch === ' ') {
      resStr = resStr.concat('%20');
    } else {
      resStr = resStr.concat(ch);
    }
  }
  return resStr;
};

function test(testName, s, expected) {
  let res = replaceSpace(s);
  console.log('res = ', res)
  if (res === expected)
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}


let s1 = "We are happy.";
let expected1 = "We%20are%20happy.";
test("test1", s1, expected1);