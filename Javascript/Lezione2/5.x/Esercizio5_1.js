let checkIfEqual = (arg1Id, arg2Id, resultId) => {
    let arg1 = document.getElementById(arg1Id).value;
    let arg2 = document.getElementById(arg2Id).value;

    if (arg1 === arg2) {
        console.log
            (`Gli argomenti forniti sono identici`);
        document.getElementById(resultId).innerText = 
            `Gli argomenti forniti sono identici`;
        return true;
    } else {
        console.log
            (`Gli argomenti forniti non sono identici`);
        document.getElementById(resultId).innerText = 
            `Gli argomenti forniti non sono identici`;
        return false;
    }
}