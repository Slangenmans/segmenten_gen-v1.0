def segmenten_gen():
    """"Deze Main function vraagt input van de gebruiker tbv het genereren van een segmentenlijst.
    Na het doorlopen van alle functies schrijft het alle data van de segmentenlijst naar een .txt bestand.
    De inhoud van dit txt bestand kan gekopieerd worden in de segmenten import sheet."""
    seg = 'Seg'
    aantal = 1

    projectcode = input("Voer projectcode in: ")
    bouwnummers = input("Voer aantal bouwnummers in: ")
    bouwnummers = int(bouwnummers)


    def gen_verd():
        """Functie returned een list object met alle verdiepingen op basis van input van de gebruiker"""
        aant_verdiepingen = input("Vul aantal verdiepingen in: ")
        aant_verdiepingen = int(aant_verdiepingen)
        verdiepingen = ["BEG-GR"]
        for i in range(1, (aant_verdiepingen + 1)):
            verdiepingen.append(f"VERD-{str(i).zfill(2)}")
        return verdiepingen


    verdiepingen = gen_verd()


    def link_verd_hoogtes():
        """"Functie returned een dictionary met de verdiepingen en hun hoogtes. Als de gebruiker geen hoogte opgeeft,
        dan zal de vorige verdiepingshoogte aangehouden worden. Hoogtes worden ingevuld door gebruiker"""
        vorige_hoogte = 0
        verd_hoogtes = {}
        for verdieping in verdiepingen:
            hoogte = input(f"Voer hoogte in voor {verdieping}: ")
            if not hoogte:
                hoogte = vorige_hoogte
            verd_hoogtes[verdieping] = hoogte
            vorige_hoogte = hoogte
            print(f"{verdieping} is {hoogte}")
        return verd_hoogtes

    verd_hoogtes = link_verd_hoogtes()

    # Om de juiste volgorde te behouden is het belangrijk dat alle cijfers hetzelfde aantal getallen bevatten.
    # De lengte van het getal wordt opgeslagen om later te gebruiken om de lengte aan te passen waar nodig.
    # Voorbeeld: Als er 420 bouwnummers zijn, dan is wordt het eerste bouwnummer geschreven als 001
    bouwnummers = str(bouwnummers)
    zerofill = len(bouwnummers)
    bouwnummers = int(bouwnummers)

    # Vanaf hier wordt de verzamelde data geschreven naar een txt bestand
    f = open('segmenten_lijst.txt', 'w')

    for verdieping in verdiepingen:
        for bouwnummer in range(1, bouwnummers+1):
            bouwnummer = str(bouwnummer).zfill(zerofill) # zfill() voegt nullen toe aan string tot opgegegeven lengte is behaald
            locatie = bouwnummer
            bnr_verd = f"BNR-{bouwnummer}-{verdieping}" # Concatonate bouwnr. met verdieping
            concate_str = f"{seg}\t{projectcode}\t{bnr_verd}\t{bnr_verd}\t{locatie}\t{verd_hoogtes[verdieping]}\t{aantal}\n"
            f.write(concate_str)
    print("Segmenten gereed!")
    f.close()


segmenten_gen()