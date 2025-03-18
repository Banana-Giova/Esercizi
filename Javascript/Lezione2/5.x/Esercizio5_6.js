let calculatorPro = (num1Id, operatorId, num2Id, resultId) => {
    
    let num1 = parseFloat(document.getElementById(num1Id).value);
    let num2 = parseFloat(document.getElementById(num2Id).value);
    let operator = document.querySelector(`input[name="${operatorId}"]:checked`).value;

    if (isNaN(num1) || isNaN(num2)) {
        operator = "gabagool";
    };

    let result_html = 
        `
        <h4>Risultato:</h4>
        <div class="box">

        `

    console.log(operator);
    switch(operator) {

        case 'sum': {
            result_html +=                 
                `${num1 + num2}
                 </div>`;
            document.getElementById(resultId).innerHTML = result_html;
            break;
        }
        case 'subtract': {
            result_html +=                 
                `${num1 - num2}
                 </div>`;
            document.getElementById(resultId).innerHTML = result_html;
            break;
        }
        case 'multiply': {
            result_html +=                 
                `${num1 * num2}
                 </div>`;
            document.getElementById(resultId).innerHTML = result_html;
            break;
        }
        case 'divide': {
            if (num2 != 0) {
                result_html +=                 
                `${num1 / num2}
                 </div>`;
            } else {
                result_html +=                 
                `Errore, divisione per zero rilevata, selezione invalida.
                 </div>`;
            }
            document.getElementById(resultId).innerHTML = result_html;
            break;
        }
        default: {
            result_html +=                 
            `Errore selezione invalida.
             </div>`;
            document.getElementById(resultId).innerHTML = result_html;
            break;
        }
    };
}