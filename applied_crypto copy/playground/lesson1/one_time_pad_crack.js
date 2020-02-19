// Code goes here
var theapp = angular.module('onetime',[]);

theapp.controller("panagramController", ["$scope", function($scope){
$scope.panagram = [
  {"letter":'10110'},
{"letter":  '01010'},
{"letter":  '10001'},
{"letter":  '11011'},
{"letter":   '10000'},
{"letter":   '01100'},
{"letter":   '11001'},
{"letter":   '11100'},
{"letter":   '01011'},
{"letter":   '10001'},
{"letter":   '10101'},
{"letter":   '11111'},
{"letter":   '00001'},
{"letter":   '11101'},
{"letter":   '10111'},
{"letter":   '11110'},
{"letter":   '01110'},
{"letter":   '01001'},
{"letter":   '01000'},
{"letter":   '01101'},
{"letter":   '11101'},
{"letter":   '01111'},
{"letter":   '11000'},
{"letter":   '10100'},
{"letter":   '10011'},
{"letter":   '11010'},
{"letter":   '10001'},
{"letter":   '10001'},
{"letter":   '10010'}];
  
const panagram = $scope.panagram.map(letter => {
  return parseInt(letter.letter, 2)
})



// console.log(panagram)
const alphabet = {
  a: 0,
  b: 1,
  c: 2, 
  d: 3, 
  e: 4, 
  f: 5, 
  g: 6, 
  h: 7,
  i: 8,
  j: 8,
  k: 9, 
  l: 10,
  m: 11,
  n: 12,
  o: 13,
  p: 14,
  q: 15,
  r: 16,
  s: 17,
  t: 18,
  u: 19,
  v: 20,
  w: 21,
  x: 22, 
  y: 23,
  z: 24
}

const reverseAlphabetLookup = {}
for(let letter in alphabet){
  reverseAlphabetLookup[alphabet[letter]] = letter
}


// one of the panagram letters is the key b/c we know the letter "a" is is 00000, and the xor of 0 with some key will be the key itself. now we can brute force the answer using every ouptut as a possible key:


const possibleMessages = panagram.map(possibleKey => {
  let notFound = false
  const answer =  panagram.map(ct => {
    const charInt = ct ^ possibleKey
    if(!reverseAlphabetLookup[charInt]){
        notFound = true
        return
      }
    const letter = reverseAlphabetLookup[charInt].toUpperCase()
    return letter == "J" ? "I" : letter
  })
  if(notFound){ return "NOT FOUND "}
  return {[possibleKey]: answer.join('')}
})

console.log('--------------------------------------')
for(let message of possibleMessages){
  console.log(message)
}


}]
);


// {25: "QUICKWAFTINGZEPHYRSVEXBOLDIIM"}

// Quick wafting zephyrs vex bold Jim