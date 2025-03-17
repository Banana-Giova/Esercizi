let numero1 = 100;

let showNumero = (id) => {
    console.log(numero1);
    document.getElementById(id).innerText = 
        `Valore del numero: ${numero1}`;
};

let changeNumero = (id) => {
    numero1 -= 30;
    showNumero(id);
};