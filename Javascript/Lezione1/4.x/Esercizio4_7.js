let calcBiggest = (formId, resultId) => {
    const form = document.getElementById(formId);
    let numbers = [];
    const inputs = form.querySelectorAll('input[type="number"]');


    for (let input of inputs) {
        let value = parseInt(input.value);
        if (!isNaN(value)) {
            numbers.push(value);
        } else {
            throw new TypeError("Inserire SOLO numeri interi.")
        }
    }
    
    console.log
        (`Il numero più grande è ${Math.max(...numbers)}`);
    document.getElementById(resultId).innerText = 
        `Il numero più grande è ${Math.max(...numbers)}`;
}