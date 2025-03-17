const curr_anno = 2025;

let calcAging = (intId, resultId) => {

    const anno_nascita = parseInt(document.getElementById(intId).value);
    if (anno_nascita < 1900 || anno_nascita > 2024 || isNaN(anno_nascita)) {
        throw TypeError("L'anno deve essere fra il 1900 e l'anno corrente.")
    }

    const curr_age = curr_anno - anno_nascita;
    const hundred = 100 - curr_age;

    console.log
        (`Se non hai compiuto gli anni, ne hai ${curr_age-1},\nSennò hai ${curr_age} anni!\nE fra ${hundred} anni ne farai 100!`);
    document.getElementById(resultId).innerText = 
        `Se non hai compiuto gli anni, ne hai ${curr_age-1},\nSennò hai ${curr_age} anni!\nE fra ${hundred} anni ne farai 100!`;
}