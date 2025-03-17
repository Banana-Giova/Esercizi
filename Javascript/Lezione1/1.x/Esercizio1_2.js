let numero = 100;

let showNumero = (id) => {
    console.log(numero);
    document.getElementById(id).innerText = 
        `Valore del numero: ${numero}`;
};

let changeNumero = (id) => {
    numero = numero - 30;
    showNumero(id);
};