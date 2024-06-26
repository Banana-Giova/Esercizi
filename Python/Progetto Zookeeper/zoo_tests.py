from zoo import Zoo, Animal, Fence, ZooKeeper


"""
Creaiamo un sistema di gestione di uno zoo virtuale
Sistema di gestione dello zoo virtuale

-Classi:
1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.
2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: 
 name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).
3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. 
  I recinti possono contenere uno o più animali. 
  I recinti possono hanno gli attributi area, temperature e habitat.
4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. 
  I guardiani dello zoo hanno un name, un surname, e un id. 
  Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

- Funzionalità:
1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): 
  Consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. 
  L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat 
  e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.
2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): 
  Consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. 
  Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.
3. feed(animal: Animal) (Dai da mangiare agli animali): 
  Implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
  Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, 
  ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. 
  Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.
4. clean(fence: Fence) (Pulizia dei recinti): 
  Implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. 
  Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
  Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. 
  Se l'area residua è pari a 0, restituire l'area occupata.
5. describe_zoo() (Visualizza informazioni sullo zoo): 
  Visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

- E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, 
e un recinto Fence(area=100, temperature=25, habitat=Continentale) 
con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) 
ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

    Guardians:

    ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

    Fences:

    Fence(area=100, temperature=25, habitat=Continent)

    with animals:

    Animal(name=Scoiattolo, species=Blabla, age=25)

    Animal(name=Lupo, species=Lupus, age=14)
    ##############################

    Fra un recinto e l'altro mettete 30 volte il carattere #.
"""


#When multiplying floats round by 3.

#Create a global/class dictionary,
#containing fences(classes) and animals in them(list of classes)



lorenzina:ZooKeeper = ZooKeeper(name="Lorenzo", 
                                surname="Maggi", 
                                id="1234")

lorenzino:ZooKeeper = ZooKeeper(name="Lorenzo", 
                                surname="Trombini", 
                                id="5678")

continental:Fence = Fence(area=0, 
                          temperature=25, 
                          habitat="Continent")

mexico:Fence = Fence(area=0, 
                          temperature=29, 
                          habitat="Carlos")

squirrel:Animal = Animal(name=None, 
                         species="Scoiatolus", 
                         age="sus",
                         height=0, width=0,
                         preferred_habitat="Continent")

wolf:Animal = Animal(name="Lupo", 
                     species="Lupus", 
                     age=None,
                     height="sus", width=0,
                     preferred_habitat="Continent")

scronf:Animal= Animal(name="Gorb",
                      species="Zorpal",
                      age=32,
                      height="sus", width=4,
                      preferred_habitat="Carlos")

biomarco:Zoo = Zoo(fences=[continental],
                   zoo_keepers=[lorenzina])

biomuchaco:Zoo = Zoo(fences=[mexico],
                     zoo_keepers=[lorenzino])



lorenzina.add_animal(squirrel, continental)
lorenzina.add_animal(wolf, continental)
lorenzino.add_animal(scronf, mexico)

biomarco.describe_zoo()
print(lorenzina.clean(continental))
lorenzina.feed(wolf)
lorenzina.remove_animal(squirrel, continental)
biomarco.describe_zoo()
print(lorenzina.clean(continental))
lorenzino.add_animal(scronf, mexico)
biomuchaco.describe_zoo()
print(lorenzino.clean(mexico))