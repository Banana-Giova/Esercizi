let calcForSumNAvg = (formId, resultId) => {
    const form = document.getElementById(formId);
    let numbers = [];
    const inputs = form.querySelectorAll('input[type="number"]');

    for (let input of inputs) {
        numbers.push(parseInt(input.value));
    }

    const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0)
    const avg = sum / numbers.length;
    
    console.log
        (`La somma dei numeri è ${sum}\nLa media dei numeri è ${avg}`);
    document.getElementById(resultId).innerText = 
        `La somma dei numeri è ${sum}\nLa media dei numeri è ${avg}`;
}