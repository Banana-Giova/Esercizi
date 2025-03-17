let x, y, z;

let showX = (id) => {
    x = 10;
    console.log
        (`Valore di X = ${x}, tipo della variabile ${typeof(x)}`);
    document.getElementById(id).innerText = 
        `Valore di X = ${x}, tipo della variabile "${typeof(x)}"`
}

let showY = (id) => {
    y = x;
    console.log
        (`Valore di Y = ${y}, tipo della variabile ${typeof(y)}`);
    document.getElementById(id).innerText = 
        `Valore di Y = ${y}, tipo della variabile "${typeof(y)}"`
}

let showZ = (id) => {
    z = "Mariangela";
    console.log
        (`Valore di Z = ${z}, tipo della variabile ${typeof(z)}`);
    document.getElementById(id).innerText = 
        `Valore di Z = ${z}, tipo della variabile "${typeof(z)}"`
}