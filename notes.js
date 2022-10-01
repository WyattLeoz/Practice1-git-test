



/*
Array

let fruit = ["orange", "banana"];


Push
Pop
unshift
shift

length
indexOf


console.log(fruit[1]);
*/
let prices = [5, 10, 15, 20];

for(let i = 0; i < prices.length; i+=1){
    console.log(prices[i]);
}

const x = 21
var y = function () {


    var x = 30;
    console.log(x);
}
y()




let grades = [10, 100, 50, 80, 70];

grades = grades.sort(aSort);
 
grades.forEach(printout);
grades.forEach(element => console.log(element));

function aSort(x, y) {
    return y - x;
}

function printout(element) {
    console.log(element);
}





let cards = ["A", "B", "C", "D", "E"];

shuffle(cards);

console.log(cards);
cards.forEach(card => console.log(card + cards.indexOf(card)))

function shuffle (array) { //elementInCardsArray
    let currentIndex = cards.length; //or array.length
    console.log(array);
    console.log(cards);
    console.log(currentIndex)

    while (currentIndex != 0) {
        let randomIndex = Math.floor(Math.random() * cards.length); //or array.length
        currentIndex-= 1;

        let temp = array[currentIndex]; //or cards[currentIndex]
        array[currentIndex] = array[randomIndex];
       array[randomIndex] = temp;
    }

    return array

}
console.log(cards);




const store = new Map([
    ["t-shirt", 20],
    ["jeans", 30],
    ["banana", 2]
])

store.forEach((value, key) => console.log(`${key} $${value}`));