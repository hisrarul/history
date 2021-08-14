const name = 'Israr'
let age = 28
let hasHobbies = true

function userSummary (name, age, hasHobbies) {
    return (
        "User is " + name +
        ", age is " + age +
        " and the user has hobbies: " + hasHobbies
    );
};

const SummarizeUser = (name, age, hasHobbies) => {
    return (
        "User is " + name +
        ", age is " + age +
        " and the user has hobbies: " + hasHobbies
    );
};

// const add = (a, b) => {
//     return a + b;
// };


const add = (a, b) => a + b;

const addOne = a => a + 1;

const addRandom = () => 1 + 2;


console.log(userSummary('Israrul', 28, true))
console.log(SummarizeUser('Kamran', 14, true))
console.log(add(5, 2))
console.log(addOne(34))
console.log(addRandom())


// Create Object and an object can also have function

const person = {
    name: 'Israr',
    age: 28,
    greet() {
        console.log('Hi, I am ' + this.name);
    }
}

console.log(person)
person.greet();

// Arrays
const hobbies = ["Sports", "cooking"]
for (let hobby of hobbies) {
    console.log(hobby);
}

console.log(hobbies.map(hobby => 'Hobby: ' + hobby));
console.log(hobbies);