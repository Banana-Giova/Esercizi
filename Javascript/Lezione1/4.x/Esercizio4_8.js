let calcOddEven = (formId, resultId) => {
    const form = document.getElementById(formId);
    const inputs = form.querySelectorAll('input[type="number"]');
    let pari = 0;
    let dispari = 0;

    for (let input of inputs) {
        let value = parseInt(input.value);
        if (isNaN(value))
            throw new TypeError("Inserire SOLO numeri interi.");

        if (value % 2) {
            ++pari;
        } else {
            ++dispari;
        }
    }
    
    console.log
        (`Nell'array ci sono ${pari} numeri pari e ${dispari} numeri dispari.`);
    document.getElementById(resultId).innerText = 
        `Nell'array ci sono ${pari} numeri pari e ${dispari} numeri dispari.`;
}