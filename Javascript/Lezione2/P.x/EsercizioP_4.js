let job1C = (resultId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
           resolve(document.getElementById(resultId).innerHTML =
                `<div class=box><h4 id="${resultId}">Sono nella callback 1</h4></div>`);
        }, 2000);
    });
}

let job2C = (resultId, repetition=0) => {
    let again = "di nuovo "
    
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            document.getElementById(resultId).innerHTML =
                `<div class=box><h5 id="${resultId}">Sono nella callback 2 ${again.repeat(repetition++)}</h5></div>`;
            resolve(repetition);
        }, 1000);
    })
}

let jobP4 = (resultId) => {
    job1C(resultId)
        .then( () => {
        return job2C(resultId)}
    ).then( (numJ2) => {
        return job2C(resultId, numJ2)}
    ).then( (numJ2) => {
        return job2C(resultId, numJ2)}
    ).catch(error => console.error(error));
}