let convertToHours = (intId, resultId) => {
    
    let raw_time = parseInt(document.getElementById(intId).value);
    if (raw_time < 1) {
        throw TypeError("Il numero deve essere positivo.")
    }

    const ore = Math.floor(raw_time / 3600);
    const minuti = Math.floor((raw_time % 3600) / 60);
    const secondi = raw_time % 60;

    console.log
        (`${ore} ore, ${minuti} minuti, ${secondi} secondi`);
    document.getElementById(resultId).innerText =
        `${ore} ore, ${minuti} minuti, ${secondi} secondi`;
    
}