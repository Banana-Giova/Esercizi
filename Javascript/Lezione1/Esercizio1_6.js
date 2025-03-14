const numbers = [47, 74, 65, 56, 33];

let showNumbers = (id) => {
    console.log(numbers);
    document.getElementById(id).innerText = numbers;
}

let showSumNAvg = (id) => {
    const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0)
    const avg = sum / numbers.length;
    
    console.log
        (`La somma dei numeri è ${sum}\nLa media dei numeri è ${avg}`);
    document.getElementById(id).innerText = 
        `La somma dei numeri è ${sum}\nLa media dei numeri è ${avg}`;
}