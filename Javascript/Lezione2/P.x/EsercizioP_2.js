let jobP2 = (numId, resultId) => {
    num = parseFloat(document.getElementById(numId).value);

    return new Promise((resolve, reject) => {
        if (isNaN(num)) {
            reject(document.getElementById(resultId).innerHTML = 
                    `<div class=box>Errore, input invalido.</div>`)
        } else {
            setTimeout(() => {
                if ((num % 2) === 0) {
                    resolve(document.getElementById(resultId).innerHTML = 
                        `<div class=box>Pari</div>`)
                } else {
                    resolve(document.getElementById(resultId).innerHTML = 
                        `<div class=box>Dispari</div>`)
                }
            }, 2000)
        }
    });
}