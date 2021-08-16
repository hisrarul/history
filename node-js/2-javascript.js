// Destructuring

const person = {
    name: 'Israr',
    age: 28,
    greet() {
        console.log('Hi, I am ' + this.name)
    }
};

const printName = ({ name }) => {
    console.log(name);
}

printName(person);

const {name, age } = person;
console.log(name, age);

const hobbies = ['sports', 'cooking'];
const [hobby1, hobby2] = hobbies;
console.log(hobby1, hobby2);

// Async code and promises

setTimeout(() => {
    console.log('Timer is done!');
},2000);

console.log('Hello!');
console.log('Hi!');

const fetchData = callback => {
    setTimeout(() => {
        callback('Done!');
    }, 1500);
};

setTimeout(() => {
    fetchData(text => {
        console.log(text);
    });
},2000);

console.log('Callback ran successfully!')

// Promises
 const fetchData = () => {
     const promise = new Promise((resolve, reject) => {
         setTimeout(() => {
             resolve('Done!');
         }, 1500);
     });
     return promise;
 };

 setTimeout(() => {
     console.log('Timer is done!');
     fetchData()
        .then(text  => {
            console.log(text);
            return fetchData();
        })
        .then(text2 => {
            console.log(text2);
        });
 }, 2000);  
