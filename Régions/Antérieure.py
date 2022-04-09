region = ""
exclusion=""
oeil=""
mode=""
ethnie=""
genre=""


def regionAnterieure(region, exclusion, oeil, mode, ethnie, genre):
    maladieUne = "Aucune"
    maladieDeux = "Aucune"
    maladieTrois = "Aucune"
    if region == "Antérieure" :
        if exclusion !=("sarcoidose" or "syphilis" or "sérologie syphilis positive" or "sarcoidose prouvée" or"eruption de zona" or "sérologie tréponémique positive"):
            if oeil == "unilatéral":
                if mode == "aigu":
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne="VZV"
                            maladieDeux="HSV"
                            maladieTrois="HLA B27"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                    elif ethnie == "asiatique":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                elif mode == "récurrent":
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                    elif ethnie == "asiatique":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "HLA B27"
                elif mode == "chronique":
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "asiatique":
                        maladieUne = "VZV"
                        maladieDeux = "HSV"
                        maladieTrois = "Arthrite chronique juvénile"
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                else:
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "asiatique":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "VZV"
                            maladieDeux = "HSV"
                            maladieTrois = "Arthrite chronique juvénile"
            elif oeil == "à bascule":
                if mode == "aigu":
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "asiatique":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                elif mode == "récurrent":
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "asiatique":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                elif mode == "chronique":
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "asiatique":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                else:
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "asiatique":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
                        elif genre == "homme":
                            maladieUne = "HLA B27"
                            maladieDeux = "HSV"
                            maladieTrois = "VZV"
            elif oeil == "bilatéral" :
                if mode == "aigu":
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                    elif ethnie == "asiatique":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                elif mode == "récurrent":
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                    elif ethnie == "asiatique":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                elif mode == "chronique":
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois="Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "asiatique":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                else:
                    if ethnie == "blanc":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "noir":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "asiatique":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                    elif ethnie == "hispanic":
                        if genre == "femme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
                        elif genre == "homme":
                            maladieUne = "Behcet"
                            maladieDeux = "SEP"
                            maladieTrois = "Arthrite chronique juvénile"
    return maladieUne,maladieDeux,maladieTrois

print(regionAnterieure("Antérieure","","unilatéral","chronique","blanc","femme"))
