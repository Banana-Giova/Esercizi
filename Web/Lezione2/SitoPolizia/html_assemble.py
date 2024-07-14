def int_inputter() -> int:
    """
        This function allows the user to input an int easily, 
        without incurring in errors if the number is not valid.
    """
    inputted_number = ""
    while True:
        
        inputted_number = input("Inserire numero di cards da iniettare nella pagina:\n>>> ")
        try:
            int(inputted_number)
            break
        except ValueError:
            print("Errore, inserire un numero valido.")
            inputted_number = ""
            continue

    return int(inputted_number)

with open('home.html', 'w') as html_file:
    html_file.write(
        """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href='data/Polizia-Di-Stato-Logo.png'>
    <title>Polizia di Stato</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
</head>
<header>

</header>
<body>
    <img src="data/logo-polizia.jpg" width="700" height="400">
    <br>
    <p>
        <h1 id="testopazzo">ULTIMORA</h1>
        <h2>La notizia che ha sconvolto la Calabria!</h2>
        <h3 class="testocalmo">Annuncio ufficiale: Osama catturato</h3>
        <a href="servizi.html" target="_blank" type="button" class="btn btn-primary">Clicca qui per scoprire i nostri servizi!</a>
    </p>
    <hr>
    <h2>Bacheca Ricercati</h2>
        """
        )
    
cards:int = int(input("Inserire numero di cards da iniettare nella pagina:\n>>> "))

with open('home.html', 'a') as html_file:
    html_file.write(
        """
    <div class="container text-center">
        <div class="row" style="padding:5%">
    """
    )

    for i in range(cards):
        html_file.write(
            """
                <div class="col-sm-3 mb-10 mb-sm-0 mt-4"">
                  <div class="card" style="width: 18rem;">
                    <img src="data/VadeRicercato.png" class="card-img-top" alt="darth-pic" width="400" height="280">
                      <div class="card-body">
                        <h5 class="card-title">RICERCATO: Darth Vader</h5>
                        <hr>
                        <p class="card-text">Avete visto nel vostro quartiere un losco individuo dal respiro pesante, con un minaccioso casco ed una potente spada laser? In tal caso attenzione, si tratta di un criminale intergalattico!</p>
                        <a href="#" class="btn btn-primary">Contattaci!</a>
                  </div>
                </div>
              </div>
        """
        )

    html_file.write(
        """
                  
            </div>
        </div>
    </div>
</body>
</html>
    """
    )
