let job1 = (resultId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
           resolve(document.getElementById(resultId).innerHTML =
                `<div class=box><h3 id="${resultId}">Ciao Mondo...</h3></div>`)
        }, 5000)
    })
}

let job2 = (resultId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(document.getElementById(resultId).innerHTML =
                `<div class=box><h4 id="${resultId}">Ciao Mondo..</h4></div>`)
        }, 2500)
    })
}

let job3 = (resultId) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(document.getElementById(resultId).innerHTML =
                `<div class=box><h5>Ciao Mondo.</h5></div>`)
        }, 1250)
    })
}

let jobP3 = async (resultId) => {
    await job1(resultId);
    await job2(resultId);
    await job3(resultId);
}