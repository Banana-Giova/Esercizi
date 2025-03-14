let weekdays = "Lunedì, Martedì, Mercoledì, Giovedì, Venerdì, Sabato, Domenica";

let showWeekdays = (id) => {
    console.log(weekdays.replace(/,/g, "\n"));
    document.getElementById(id).innerText = weekdays.replace(/,/g, "\n");
}