accounts = []
provinces = []
parties = []
assembly = []
usednames = []


def condep():  # This method allows the user to check the distribution of the legislative assembly
    if len(provinces) == 0:
        print("Territorial distribution has been created, you will be returned to the consultation menu")
        menucon()
    else:
        for prov in provinces:
            print("Province: " + prov["Name"] + ". Amount of deputies: " + prov["Deputies"])
            totaldepu = 0
            for part in prov["LegBall"]:
                part["Deputies"] = part["LegVotes"] // prov["Coeficient"]
                totaldepu = totaldepu + part["Deputies"]
            if totaldepu < int(prov["Deputies"]):
                for par in prov["LegBall"]:
                    remvotes = par["LegVotes"] - (par["Deputies"] * prov["Coeficient"])
                    par["Deputies"] = par["Deputies"] + (remvotes // prov["Subcoeficient"])
            for pa in prov["LegBall"]:
                depus = {"Name": pa["Name"], "Deputies": str(pa["Deputies"])}
                assembly.append(depus)
            for party in assembly:
                print(party["Name"] + ": " + party["Deputies"])


def calculegis():  # This method calculates the total legislative votes across all provinces and cantons
    for prov in provinces:
        for cant in prov["Cantons"]:
            for party in cant["LegBall"]:
                totvotes = 0
                for dist in cant["Districts"]:
                    for part in dist["LegBall"]:
                        if part["ID"] == party["ID"]:
                            totvotes = totvotes + part["LegVotes"]
                party["LegVotes"] = totvotes
    for provin in provinces:
        for pa in provin["LegBall"]:
            totalvotes = 0
            for canto in provin["Cantons"]:
                for par in canto["LegBall"]:
                    if par["ID"] == pa["ID"]:
                        totalvotes = totalvotes + par["LegVotes"]
            pa["LegVotes"] = totalvotes
    for province in provinces:
        sumvotes = 0
        for part in province["LegBall"]:
            sumvotes = sumvotes + part["LegVotes"]
        coefi = sumvotes // int(province["Deputies"])
        subcoe = coefi / 2
        province["Coeficient"] = coefi
        province["Subcoeficient"] = subcoe
    condep()


def condis():  # This method allows the user to check the electoral
    if len(provinces) == 0:
        print("Territorial distribution has not been created, you will be returned to the consultation menu")
        menucon()
    else:
        for prov in provinces:
            print("Province: " + prov["Name"])
            for cant in prov["Cantons"]:
                print("Canton: " + cant["Name"])
                for dist in cant["Districts"]:
                    winner = []
                    maxvotes = 0
                    print("District: " + dist["Name"])
                    for party in dist["PresBall"]:
                        maxvotes += party["PresVotes"]
                        winner.append(party)
                    for pa in dist["PresBall"]:
                        pa["PresPor"] = (pa["PresVotes"] * 100) / maxvotes
                        print(pa["Name"] + ": " + str(pa["PresVotes"]) + ". " + str(pa["PresPor"]) + "%.")
                    win = winner[0]
                    for part in winner:
                        if part["PresVotes"] > win["PresVotes"]:
                            win = part
                    print("Winner: " + win["Name"])


def concan():  # This method allows the user to check the electoral results by canton
    if len(provinces) == 0:
        print("Territorial distribution has not been created, you will be returned to the consultation menu")
        menucon()
    else:
        for prov in provinces:
            print("Province: " + prov["Name"])
            for cant in prov["Cantons"]:
                winner = []
                maxvotes = 0
                print("Canton: " + cant["Name"])
                for part in cant["PresBall"]:
                    maxvotes += part["PresVotes"]
                    winner.append(part)
                for pa in cant["PresBall"]:
                    pa["PresPor"] = (pa["PresVotes"] * 100) / maxvotes
                    print(pa["Name"] + ": " + str(pa["PresVotes"]) + ": " + str(pa["PresPor"]) + "%.")
                win = winner[0]
                for par in winner:
                    if par["PresVotes"] > win["PresVotes"]:
                        win = par
                print("Winner: " + win["Name"])


def conprov():  # This method allows the user to consdult the electorsal results by province
    if len(provinces) == 0:
        print("Territorial distribution has not been created, you will be returned to the consultation menu")
        menucon()
    else:
        for prov in provinces:
            winner = []
            print("Province: " + prov["Name"])
            maxvotes = 0
            for part in prov["PresBall"]:
                maxvotes += part["PresVotes"]
                winner.append(part)
            for pa in prov["PresBall"]:
                pa["PresPor"] = (pa["PresVotes"] * 100) / maxvotes
                print(pa["Name"] + ": " + str(pa["PresVotes"]) + ". " + str(pa["PresPor"]) + "%.")
            win = winner[0]
            for par in winner:
                if par["PresVotes"] > win["PresVotes"]:
                    win = par
            print("Winner: "+ win["Name"])


def connat():  # This methods allows the user to consult the total electoral results across the country
    if len(provinces) == 0:
        print("Territorial distribution has not been created, you will be returned to the consultation menu")
        menucon()
    else:
        winner = []
        natpresball = provinces[0]["PresBall"]
        maxvotes = 0
        for p in natpresball:
            tovot = 0
            for pro in provinces:
                for partie in pro["PresBall"]:
                    if partie["ID"] == p["ID"]:
                        tovot = tovot + partie["PresVotes"]
            p["PresVotes"] = tovot
            maxvotes = maxvotes + p["PresVotes"]
            winner.append(p)
        for party in natpresball:
            party["PresPor"] = (party["PresVotes"] * 100) / maxvotes
            print(party["Name"] + ": " + str(party["PresVotes"]) + ". " + str(party["PresPor"]) + "%.")
        win = winner[0]
        for part in winner:
            if part["PresVotes"] > win["PresVotes"]:
                win = part
        print("Winner: "+ win["Name"])


def menucon():  # This menu asks the user which type of consultation they want to make
    print("These are the type of consultation available: \n"
          "1) National results.\n"
          "2) Provincial results.\n"
          "3) Cantonal results.\n"
          "4) District results\n"
          "5) Legislative assembly conformation.\n"
          "6) Back")
    choi13 = input("Select an option: ")
    if choi13 == "1":
        print("You have chosen to check the national election result.")
        connat()
        menucon()
    elif choi13 == "2":
        print("You have chosen to check the results of each province.")
        conprov()
        menucon()
    elif choi13 == "3":
        print("You have chosen to check the results by cantons.")
        concan()
        menucon()
    elif choi13 == "4":
        print("You have chosen to check the results by districts.")
        condis()
        menucon()
    elif choi13 == "5":
        print("You have chosen to check the conformation of the legislative assembly.")
        calculegis()
        menucon()
    elif choi13 == "6":
        print("You have chosen to go back to the previous menu.")
        menuadmin()
    else:
        print("Invalid option, please choose a valid option.")
        menucon()


def calculator():  # This method makes the calculates the presidential votes for each party across the provinces and cantons
    p = 0
    while p < len(provinces):
        c = 0
        while c < len(provinces[p]["Cantons"]):
            d = 0
            while d < len(provinces[p]["Cantons"][c]["Districts"]):
                pp = 0
                while pp < len(provinces[p]["Cantons"][c]["Districts"][d]["PresBall"]):
                    if provinces[p]["Cantons"][c]["Districts"][d]["PresBall"][pp]["ID"] == \
                            provinces[p]["Cantons"][c]["PresBall"][pp]["ID"]:
                        votesori = provinces[p]["Cantons"][c]["Districts"][d]["PresBall"][pp]["PresVotes"]
                        provinces[p]["Cantons"][c]["PresBall"][pp]["PresVotes"] = int(
                            provinces[p]["Cantons"][c]["PresBall"][pp]["PresVotes"]) + int(
                            provinces[p]["Cantons"][c]["Districts"][d]["PresBall"][pp]["PresVotes"])
                        provinces[p]["PresBall"][pp]["PresVotes"] = int(
                            provinces[p]["PresBall"][pp]["PresVotes"]) + int(
                            provinces[p]["Cantons"][c]["Districts"][d]["PresBall"][pp]["PresVotes"])
                        provinces[p]["Cantons"][c]["Districts"][d]["PresBall"][pp]["PresVotes"] = votesori
                    pp += 1
                d += 1
            c += 1
        p += 1
    menucon()


def modLesRes():  # This method allows the user to modify the legilstive results
    if len(provinces) == 0:
        print("No registered provinces have been found. You will be redirected to the Results Menu")
        menuResults()
    elif len(provinces[0]["LegBall"]) == 0:
        print("The presidential ballots are empty, you will be redirected to the Results Menu")
        menuResults()
    else:
        for pro in provinces:
            print(pro["Name"] + ": " + pro["Code"])
        provco = input("Insert the province code: ")
        if provco.isdigit() and int(provco) in range(1, len(provinces) + 1):
            for can in provinces[int(provco) - 1]["Cantons"]:
                print(can["Name"] + ": " + can["Number"])
            cantco = input("Insert canton number: ")
            if cantco.isdigit() and int(cantco) in range(1, len(provinces[int(provco) - 1]["Cantons"]) + 1):
                for dist in provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"]:
                    print(dist["Name"] + ": " + dist["Number"])
                distco = input("Insert district code: ")
                if distco.isdigit() and int(distco) in range(1, len(
                        provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"]) + 1):
                    for part in provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"][int(distco) - 1][
                        "LegBall"]:
                        votes = input(part["Name"])
                        if votes.isdigit():
                            part["LegVotes"] = int(votes)
                        else:
                            print("Invalid amount of votes, reinsert data.")
                            modLesRes()
                else:
                    print("Invalid district number, reinsert data")
                    modLesRes()
            else:
                print("Invalid canton number, reinsert data.")
                modLesRes()
        else:
            print("Invalid province code, reinsert data,")
            modLesRes()
        menuResults()


def modPresRes():  # This method allows the users to modify the presidential results
    if len(provinces) == 0:
        print("No registered provinces have been found. You will be redirected to the Results Menu")
        menuResults()
    elif len(provinces[0]["PresBall"]) == 0:
        print("The presidential ballots are empty, you will be redirected to the Results Menu")
        menuResults()
    else:
        for pro in provinces:
            print(pro["Name"] + ": " + pro["Code"])
        provco = input("Insert the province code: ")
        if provco.isdigit() and int(provco) in range(1, len(provinces) + 1):
            for can in provinces[int(provco) - 1]["Cantons"]:
                print(can["Name"] + ": " + can["Number"])
            cantco = input("Insert canton number: ")
            if cantco.isdigit() and int(cantco) in range(1, len(provinces[int(provco) - 1]["Cantons"]) + 1):
                for dist in provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"]:
                    print(dist["Name"] + ": " + dist["Number"])
                distco = input("Insert district code: ")
                if distco.isdigit() and int(distco) in range(1, len(
                        provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"]) + 1):
                    for part in provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"][int(distco) - 1][
                        "PresBall"]:
                        votes = input(part["Name"])
                        if votes.isdigit():
                            part["PresVotes"] = int(votes)
                        else:
                            print("Invalid amount of votes, reinsert data.")
                            modPresRes()
                else:
                    print("Invalid district number, reinsert data")
                    modPresRes()
            else:
                print("Invalid canton number, reinsert data.")
                modPresRes()
        else:
            print("Invalid province code, reinsert data,")
            modPresRes()

    for prov in provinces:
        for pa in prov["PresBall"]:
            print(prov["Name"])
            print(pa["Name"] + ": " + str(pa["PresVotes"]))
        for cant in prov["Cantons"]:
            print(cant["Name"])
            for par in cant["PresBall"]:
                print(par["Name"] + ": " + str(par["PresVotes"]))
            for dist in cant["Districts"]:
                print(dist["Name"])
                for party in dist["PresBall"]:
                    print(party["Name"] + ": " + str(party["PresVotes"]))
    menuResults()


def menuResults():  # This menu asks the user which type of results they want to modify
    print("1) Presidential \n"
          "2) Legislative \n"
          "3) Back")
    choi1 = input("Which type of ballot do you want to modify?: ")
    if choi1 == "1":
        print("You've chosen to modify the Presidential Results!")
        modPresRes()
    elif choi1 == "2":
        print("You've chosen to modify the Legislative Ballots!")
        modLesRes()
        menuResults()
    elif choi1 == "3":
        print("You have chosen to go back to the previous menu")
        menuadmin()
        menuResults()
    else:
        print("Invalid input. Please enter 1 or 2 for Presidential or Legislative ballots respectively.")
        menuResults()


def delProBall():  # This method allows the user to completely delete a legislative ballot from a province
    if len(provinces) == 0:
        print("No registered provinces have been found, you will be redirected to the ballot management menu.")
        menuball()
    else:
        print("Available provinces: ")
        for prov in provinces:
            print(prov["Name"] + ": " + prov["Code"])
        provco = input("Select a province: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            if len(provinces[int(provco) - 1]["LegBall"]) == 0:
                print(
                    "The legislative ballot of this province is empty, you will be redirected to the ballot management menu.")
                menuball()
            else:
                print(
                    "Are you sure you sure you want to delete the legislative ballot of this province?(This action is irreversible).\n"
                    "1) Yes\n"
                    "2) No")
                option = input("Choose your answer: ")
                if option == "1":
                    while len(assembly) != 0:
                        assembly.pop(0)
                        provinces[int(provco) - 1]["LegBall"].pop(0)
                        for cant in provinces[int(provco) - 1]["LegBall"]:
                            cant["LegBall"].pop(0)
                            for dist in cant["Districts"]:
                                dist["LegBall"].pop(0)
                    menuball()
                    print("The legislative ballot of this province has been deleted")
                elif option == "2":
                    print(
                        "You have chosen to not delete the legislative ballot of this province. You will be returned to the ballot management menu.")
                    menuball()
                else:
                    print("Invalid option, please choose a valid option.")
                    delProBall()
        else:
            print("Invalid option, please select a valid option.")
            delProBall()


def modmore2():  # This menu allows the user choose if they want to keep modfying the presidential ballot
    print("Keep modifying the ballot?\n"
          "1) Yes\n"
          "2) No")
    choi11 = input("Choose: ")
    if choi11 == "1":
        print("You have chosen to modify the legislative ballot of the province even further.")
        menueditProBall()
    elif choi11 == "2":
        print("You have chosen to stop modifying the legislative ballot of the province.")
        menuball()
    else:
        print("Invalid option, please choose a valid option.")
        modmore2()


def chanOrPro():  # This method allows the user to change the order in which parties are shown within a legislative ballot
    if len(provinces) == 0:
        print("No registered provinces have been found, you will be redirected to the ballot management menu.")
        menuball()
    else:
        print("Available provinces: ")
        for prov in provinces:
            print(prov["Name"] + ": " + prov["Code"])
        provco = input("Select a province: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            if len(provinces[int(provco) - 1]["LegBall"]) == 0:
                print(
                    "There are no parties in this legislative ballot, you will be redirected to the ballot management menu.")
                menuball()
            else:
                for party in provinces[int(provco) - 1]["LegBall"]:
                    print(party["Name"] + ": " + party["ID"])
                movef = input("Select the party you want to move: ")
                movet = input("Select the party you want it to switch places with: ")
                p1 = 0
                while p1 < len(provinces[int(provco) - 1]["LegBall"]):
                    if movef == provinces[int(provco) - 1]["LegBall"][p1]["ID"]:
                        mof = provinces[int(provco) - 1]["LegBall"][p1]
                        namef = provinces[int(provco) - 1]["LegBall"][p1]["Name"]
                        indf = p1
                    elif movet == provinces[int(provco) - 1]["LegBall"][p1]["ID"]:
                        mot = provinces[int(provco) - 1]["LegBall"][p1]
                        namet = provinces[int(provco) - 1]["LegBall"][p1]["Name"]
                        indt = p1
                    p1 += 1
                provinces[int(provco) - 1]["LegBall"][indf] = mot
                provinces[int(provco) - 1]["LegBall"][indt] = mof
                for cant in provinces[int(provco) - 1]["Cantons"]:
                    cant["LegBall"][indf] = mot
                    cant["LegBall"][indt] = mof
                    for dist in cant["Districts"]:
                        dist["LegBall"][indf] = mot
                        dist["LegBall"][indt] = mof
                print(
                    "The political parties " + namef + " and " + namet + " have swapped places in the legislative ballot ballot.")
                modmore2()
        else:
            print("Invalid province code, reinsert data.")
            chanOrPro()


def revParProBall():  # This method allows the user to remove parties from a legislative ballot
    if len(provinces) == 0:
        print("No registered provinces have been found, you will be redirected to the ballot management menu.")
        menuball()
    else:
        print("Available provinces: ")
        for prov in provinces:
            print(prov["Name"] + ": " + prov["Code"])
        provco = input("Select a province: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            if len(provinces[int(provco) - 1]["LegBall"]) == 0:
                print(
                    "There are no parties in this legislative ballot, you will be returned to the legislative ballot modification menu.")
                menueditProBall()
            else:
                print("These are the parties currently in the ballot:")
                for party in provinces[int(provco) - 1]["LegBall"]:
                    print(party["Name"] + ": " + party["ID"])
                select = input("Select the party you want to remove: ")
                if select.isdecimal():
                    p = 0
                    while p < len(provinces[int(provco) - 1]["LegBall"]):
                        if select == provinces[int(provco) - 1]["LegBall"][p]["ID"]:
                            remoname = provinces[int(provco) - 1]["LegBall"][p]["Name"]
                            removed = provinces[int(provco) - 1]["LegBall"][p]
                            provinces[int(provco) - 1]["LegBall"].remove(removed)
                            for cant in provinces[int(provco) - 1]["Cantons"]:
                                cant["LegBall"].remove(removed)
                                for dist in cant["Districts"]:
                                    dist["LegBall"].remove(removed)
                            print("The political party " + remoname + " has been removed from the legislative ballot")
                        p += 1
                    modmore2()
                else:
                    print("Invalid party ID, reinsert data.")
                    delProBall()
        else:
            print("Invalid province code, reinsert data.")
            revParProBall()


def addPartypro():  # This method allows the user to add more parties to an already exsisting legislative ballot
    if len(parties) == 0:
        print("No registered parties have been found, you will be redirected to the ballot management menu.")
        menuball()
    elif len(provinces) == 0:
        print("No registered provinces have been found, you will be redirected to the ballot menu.")
        menuball()
    else:
        for provin in provinces:
            print(provin["Name"] + ": " + provin["Code"])
        provco = input("Select the province this ballot belongs to: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            for par in parties:
                if par["Type"] == "2" and par not in provinces[int(provco) - 1]["LegBall"]:
                    print(par["Name"] + ": " + par["ID"])
            selected = input("Insert the code of the party you want to add to the ballot: ")
            if selected.isdecimal():
                p = 0
                while p < len(parties):
                    if selected == parties[p]["ID"]:
                        provinces[int(provco) - 1]["LegBall"].append(parties[p])
                        for cant in provinces[int(provco) - 1]["Cantons"]:
                            cant["LegBall"].append(parties[p])
                            for dist in cant["Districts"]:
                                dist["LegBall"].append(parties[p])
                    p += 1
                modmore2()
            else:
                print("Invalid party code, reinsert data.")
                addPartypro()
        else:
            print("Invalid province code, reinsert data.")
            addPartypro()


def menueditProBall():  # This methods allows the way they want to modify the legislative ballot
    print("Possible modifications:\n"
          "1) Add another party to the ballot.\n"
          "2) Remove a party from the ballot.\n"
          "3) Change the order of the parties.\n"
          "4) Back.")
    choi10 = input("Select the type of modification: ")
    if choi10 == "1":
        print("You have chosen to add another party to the ballot.")
        addPartypro()
    elif choi10 == "2":
        print("You have chosen to remove a party from the ballot.")
        revParProBall()
    elif choi10 == "3":
        print("You have chosen to modify the order in which the parties are shown in the ballot.")
        chanOrPro()
    elif choi10 == "4":
        print("You have chosen to go back to the previous menu.")
        menumodball()
    else:
        print("Invalid option, please chhose a valid option.")
        menueditProBall()


def modmore():  # This method allows the user to decide if they want to keep modifying the presidential ballot even further.
    print("Keep modifying the ballot?\n"
          "1) Yes\n"
          "2) No")
    choi11 = input("Choose: ")
    if choi11 == "1":
        print("You have chosen to modify the presidential ballot even further.")
        menumodpreball()
    elif choi11 == "2":
        print("You have chosen to stop modifying the presidential ballot.")
        menuball()
    else:
        print("Invalid option, please choose a valid option.")
        modmore()


def delpresball():  # This menu allows to delete the presidential ballot completely.
    if len(provinces) == 0:
        print("Territorial distribution has not been created, you will be returned to the consultation menu")
        menucon()
    elif len(provinces[0]["PresBall"]) == 0:
        print("The presidential ballot is yet to be created, you will be returnd to the ballot management menu.")
        menuball()
    else:
        print("Are you sure you sure you want to delete the presidential ballot?(This action is irreversible).\n"
              "1) Yes\n"
              "2) No")
        option = input("Choose your answer: ")
        if option == "1":
            p = 0
            while len(provinces[0]["PresBall"]) != 0:
                for prov in provinces:
                    prov["PresBall"].pop(p)
                    for cant in prov["Cantons"]:
                        cant["PresBall"].pop(p)
                        for dist in cant["Districts"]:
                            dist["PresBall"].pop(p)
            print("The presidential ballot has been deleted")
            menuball()
        elif option == "2":
            print(
                "You have chosen to not delete the presidential ballot. You will be returned to the ballot management menu.")
            menuball()
        else:
            print("Invalid option, please select a valid option.")
            delpresball()


def menudelbal():
    print("What type of ballot do you want to delete?\n"
          "1) Presidential.\n"
          "2) Legislative\n"
          "3) Back.")
    choi12 = input("Select an option: ")
    if choi12 == "1":
        print("You have chosen to delete the presidential ballot.")
        delpresball()
    elif choi12 == "2":
        print("You have chosen to delete the legislative ballot.")
        delProBall()
    elif choi12 == "3":
        print("You have chosen to go back to the previous menu.")
        menuball()
    else:
        print("Invalid option, please choose a valid option.")
        menudelbal()


def chanorpreball():  # This method allows to change the order in which the parties show up within the presidential ballot
    if len(provinces) == 0:
        print("Territorial distribution has not been created, you will be returned to the consultation menu")
        menucon()
    elif len(provinces[0]["PresBall"]) == 0:
        print("The presidential ballot is empty, you will be redirected to the ballot management menu.")
        menuball()
    else:
        print("These are the parties currently in the ballot: ")
        for party in provinces[0]["PresBall"]:
            print(party["Name"] + ": " + party["ID"])
        movef = input("Select the party you want to move: ")
        movet = input("Select the party you want it to switch places with: ")
        p1 = 0
        while p1 < len(provinces[0]["PresBall"]):
            if movef == provinces[0]["PresBall"][p1]["ID"]:
                mof = provinces[0]["PresBall"][p1]
                namef = provinces[0]["PresBall"][p1]["Name"]
                indf = p1
            p1 += 1
        p2 = 0
        while p2 < len(provinces[0]["PresBall"]):
            if movet == provinces[0]["PresBall"][p2]["ID"]:
                mot = provinces[0]["PresBall"][p2]
                namet = provinces[0]["PresBall"][p2]["Name"]
                indt = p2
            p2 += 1
        for prov in provinces:
            prov["PresBall"][indf] = mot
            prov["PresBall"][indt] = mof
            for cant in prov["Cantons"]:
                cant["PresBall"][indf] = mot
                cant["PresBall"][indt] = mof
                for dist in cant["Districts"]:
                    dist["PresBall"][indf] = mot
                    dist["PresBall"][indt] = mof
        print("The political parties " + namef + " and " + namet + " have swapped places in the presidential ballot.")
        modmore()


def revpreball():  # This method allows to remove parties from the presidential ballot
    if len(provinces) == 0:
        print("Territorial distribution has not been created, you will be returned to the consultation menu")
        menucon()
    elif len(provinces[0]["PresBall"]) == 0:
        print("The presidential ballot is empty. You will be returned to the ballot modification menu.")
        menumodball()
    else:
        print("These are the parties currently in the ballot:")
        for party in provinces[0]["PresBall"]:
            print(party["Name"] + ": " + party["ID"])
        select = input("Select the party you want to remove: ")
        if select.isdecimal() and int(select) in range(1, len(provinces[0]["PresBall"]) + 1):
            p = 0
            while p < len(provinces[0]["PresBall"]):
                if select == provinces[0]["PresBall"][p]["ID"]:
                    remoname = provinces[0]["PresBall"][p]["Name"]
                    removed = provinces[0]["PresBall"][p]
                    for prov in provinces:
                        prov["PresBall"].remove(removed)
                        for cant in prov["Cantons"]:
                            cant["PresBall"].remove(removed)
                            for dist in cant["Districts"]:
                                dist["PresBall"].remove(removed)
                    print("The political party " + remoname + " has been removed from the presidential ballot")
                p += 1
            modmore()
        else:
            print("Invalid party ID, reinsert data.")
            revpreball()


def addpreball():  # This method allows to user to add more parties to the presidential ballots
    if len(parties) == 0:
        print("No political parties have been found, you will be redirected to the ballot management menu.")
        menucreball()
    else:
        print("This are the political parties that can be selected for presidential elections.")
        for party in parties:
            if party["Type"] == "1" and party not in provinces[0]["PresBall"]:
                print(party["Name"] + ": " + party["ID"])
        selected = input("Enter the code of the party you want to add to the ballot: ")
        p = 0
        while p < len(parties):
            if selected == parties[p]["ID"]:
                for prov in provinces:
                    prov["PresBall"].append(parties[p])
                    for canto in prov["Cantons"]:
                        canto["PresBall"].append(parties[p])
                        for distri in canto["Districts"]:
                            distri["PresBall"].append(parties[p])
                print(parties[p]["Name"] + " has been added to the presidential ballot.")
            p += 1
        modmore()


def menumodpreball():  # This method allows the user which type of modification they want to do to the presidential ballot
    print("Possible modifications:\n"
          "1) Add another party to the ballot.\n"
          "2) Remove a party from the ballot.\n"
          "3) Change the order of the parties.\n"
          "4) Back.")
    choi10 = input("Select the type of modification: ")
    if choi10 == "1":
        print("You have chosen to add another party to the ballot.")
        addpreball()
    elif choi10 == "2":
        print("You have chosen to remove a party from the ballot.")
        revpreball()
    elif choi10 == "3":
        print("You have chosen to modify the order in which the parties are shown in the ballot.")
        chanorpreball()
    elif choi10 == "4":
        print("You have chosen to go back to the previous menu.")
        menumodball()
    else:
        print("Invalid option, please chhose a valid option.")
        menumodpreball()


def menumodball():  # This method allows the user to pick which type of ballot they want to modify
    print("1) Presidential.\n"
          "2) Legislative.\n"
          "3) Back.")
    choi9 = input("Select the type of ballot you want to modify: ")
    if choi9 == "1":
        print("You have chosen to modify the presidential ballot")
        menumodpreball()
    elif choi9 == "2":
        print("You have chosen to modify the legislative ballot")
        menueditProBall()
    elif choi9 == "3":
        print("You have chosen to go back to the Ballot Management menu")
        menuball()
    else:
        print("Invalid option, please choose a valid option.")
        menumodball()


def addmore2():  # This method allows the user to choose if they want to add more parties to the ballot or not
    print("Do you wish to add more parties to the ballot?.\n"
          "1) Yes.\n"
          "2) No.")
    opt = input("Select an option: ")
    if opt == "1":
        creballpro()
    elif opt == "2":
        print("Ballot successfully created.")
        menuball()
    else:
        print("Invalid option, please select a valid option")
        addmore2()


def creballpro():  # This method allows the user to create legislative ballots
    if len(parties) == 0:
        print("No registered parties have been found, you will be redirected to the ballot management menu.")
        menuball()
    elif len(provinces) == 0:
        print("No registered provinces have been found, you will be redirected to the ballot menu.")
        menuball()
    else:
        for provin in provinces:
            print(provin["Name"] + ": " + provin["Code"])
        provco = input("Select the province this ballot belongs to: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            for par in parties:
                if par["Type"] == "2" and par not in provinces[int(provco) - 1]["LegBall"]:
                    print(par["Name"] + ": " + par["ID"])
            selected = input("Insert the code of the party you want to add to the ballot: ")
            if selected.isdigit():
                p = 0
                while p < len(parties):
                    if selected == parties[p]["ID"]:
                        provinces[int(provco) - 1]["LegBall"].append(parties[p])
                        for cant in provinces[int(provco) - 1]["Cantons"]:
                            cant["LegBall"].append(parties[p])
                            for dist in cant["Districts"]:
                                dist["LegBall"].append(parties[p])
                    p += 1
                addmore2()
            else:
                print("Invalid party code, reinsert data.")
                creballpro()
        else:
            print("Invalid province code, reinsert data.")
            creballpro()


def addmore1():  # This method allows the user to choose if they want to add more parties to the ballot or not
    print("Do you wish to add more parties to the ballot?.\n"
          "1) Yes.\n"
          "2) No.")
    opt = input("Select an option: ")
    if opt == "1":
        creballpre()
    elif opt == "2":
        print("Ballot successfully created.")
        menuball()
    else:
        print("Invalid option, please select a valid option.")
        addmore1()


def creballpre():  # This method allows to user to create presidential ballots
    if len(parties) == 0:
        print("No political parties have been found, you will be redirected to the ballot management menu.")
        menucreball()
    else:
        print("This are the political parties that can be selected for presidential elections.")
        for party in parties:
            if party["Type"] == "1" and party not in provinces[0]["PresBall"]:
                print(party["Name"] + ": " + party["ID"])
        selected = input("Enter the code of the party you want to add to the ballot: ")
        if selected.isdecimal():
            p = 0
            while p < len(parties):
                if selected == parties[p]["ID"]:
                    for prov in provinces:
                        prov["PresBall"].append(parties[p])
                        for canto in prov["Cantons"]:
                            canto["PresBall"].append(parties[p])
                            for distri in canto["Districts"]:
                                distri["PresBall"].append(parties[p])
                    print(parties[p]["Name"] + " has been added to the presidential ballot.")
                p += 1
            addmore1()
        else:
            print("Invalid party code, reinsert data.")
            creballpre()


def menucreball():  # This method allows the user to select the type of ballot they want to create
    print("What type of ballot do you want to create\n"
          "1) Presidential ballot.\n"
          "2) Legislative ballot.\n"
          "3) Back.")
    choi8 = input("Select and option: ")
    if choi8 == "1":
        print("You have chosen to create a presidential ballot.")
        creballpre()
    elif choi8 == "2":
        print("You have chosen to create a provincial ballot.")
        creballpro()
    elif choi8 == "3":
        print("You have chosen to go back to the ballot menu.")
        menuball()
    else:
        print("Invalid option, please select a valid option.")
        menucreball()


def menuball():  # This is the ballot menu
    print("1) Create ballot.\n"
          "2) Modify ballot.\n"
          "3) Delete ballot.\n"
          "4) Back.")
    choi7 = input("Please select an option: ")
    if choi7 == "1":
        print("You have chosen to create a new ballot.")
        menucreball()
    elif choi7 == "2":
        print("You have chosen to modify an existing ballot.")
        menumodball()
    elif choi7 == "3":
        print("You have chosen to delete an existing ballot.")
        menudelbal()
    elif choi7 == "4":
        print("You have chosen to go back to the administrator menu.")
        menuadmin()
    else:
        print("Invalid option, please choose a valid option.")
        menuball()


def dellPartie():  # This method allows to delete political parties
    if len(parties) == 0:
        print("No political parties have been found, you will be redirected to the Political Parties menu.")
        menupart()
    else:
        for par in parties:
            print(par["Name"] + ": " + par["ID"])
        dell = input("Select the Political Party you want to delete: ")
        if dell.isdigit() and int(dell) in range(1, len(parties) + 1):
            i = 0
            while i < len(parties):
                if dell == parties[i]["ID"]:
                    savedpart = parties[i]
                    parties.remove(savedpart)
                    print("Political Party deleted!")
        else:
            print("Invalid party code, reinsert data.")
            dellPartie()


def modPartie():  # This menu allows to modify existing political parties
    if len(parties) == 0:
        print("No political parties have been found, you will be redirected to the Political Parties menu.")
        menupart()
    else:
        for par in parties:
            print(par["Name"] + ": " + par["ID"])
        iden = input("Now, enter the number of the Political Partie you want to modify: ")
        if iden.isdigit() and int(iden) in range(1, len(parties) + 1):
            for party in parties:
                if iden == party["ID"]:
                    print("Please add the Political Party's info: ")
                    newname = input("Enter the Political Party's new name: ")
                    if newname.upper() in usednames:
                        print("Name already taken, reinsert data.")
                        modPartie()
                    else:
                        oldname = party["Name"]
                        party["Name"] = newname
                        party["Year"] = input("Enter the new Foundation Year: ")
                        party["Colors"] = input("Enter the new Political Party's colors: ")
                        party["Ideas"] = input("Enter the new ideological stream: ")
                        newnamed = newname.upper()
                        usednames.append(newnamed)
                        oldnamed = oldname.upper()
                        usednames.remove(oldnamed)
                        print("You've successfully changed the party´s information.")
        else:
            print("Invalid party code, reinsert data.")
            modPartie()


def newPartie():  # This method allows to add new political parties
    print("Enter the type of political party: ")
    type = input("National(1) or Provincial(2): ")
    if type.isdecimal() and int(type) in range(1, 3):
        print("Now, please add the Political Party's info: ")
        iden = str(len(parties) + 1)
        name = input("Name: ")
        if name.upper() in usednames:
            print("Name already taken, reinsert data.")
            newPartie()
        else:
            year = input("Foundation year: ")
            clrs = input("Representing colours: ")
            idea = input("Ideological stream: ")
            nPartie = {"ID": iden, "Name": name, "Year": year, "Colors": clrs, "Ideas": idea, "Type": type,
                       "PresVotes": 0, "LegVotes": 0, "PresPor": 0, "Deputies": 0}
            parties.append(nPartie)
            named = name.upper()
            usednames.append(named)
            print(" Success! You have added a new Political Partie to the system.")
    else:
        print("Invalid party type, reinsert data.")
        newPartie()


def menupart():  # This menu allows to manage the political parties
    print("This is the Political Parties' menu. Please choose an option: \n"
          "1) Add new Political Party.\n"
          "2) Modify an existing Political Party.\n"
          "3) Delete a Political Party.\n"
          "4) Back.")
    choice1 = input("Your choice: ")
    if choice1 == "1":
        print("You have chosen to create a new political party.")
        newPartie()
        menupart()
    elif choice1 == "2":
        print("You have chosen to modify an existing political party")
        modPartie()
        menupart()
    elif choice1 == "3":
        print("You have chosen to delete one of the political parties.")
        dellPartie()
        menupart()
    elif choice1 == "4":
        print("You have chosen to go back to the administrator menu")
        menuadmin()
    else:
        print("Invalid input. Please enter a valid input. ")
        menupart()


def deldis():  # This method allows to delete district
    if len(provinces) == 0:
        print("No registered provinces have been found, you will be redirected to the territorial distribtion menu")
        menuprovin()
    else:
        for provin in provinces:
            print(provin["Name"] + ": " + provin["Code"])
        provco = input("Select the province the canton belongs to: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            if len(provinces[int(provco) - 1]["Cantons"]) == 0:
                print(
                    "No registered cantons have been found in this province, you will be redirected to the territorial distribution menu")
                menuprovin()
            else:
                for cant in provinces[int(provco) - 1]["Cantons"]:
                    print(cant["Name"] + ": " + cant["Number"])
                cantco = input("Select the canton the distric belongs to: ")
                if cantco.isdecimal() and int(cantco) in range(1, len(provinces[int(provco) - 1]["Cantons"]) + 1):
                    if len(provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"]) == 0:
                        print(
                            "No registered districts have been found in this canton, you will be redirected to the teeritorial distribution menu")
                        menuprovin()
                    else:
                        for dist in provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"]:
                            print(dist["Name"] + ": " + dist["Number"])
                        distco = input("Select the district you want to delete: ")
                        if distco.isdecimal() and int(distco) in range(1, len(
                                provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"]) + 1):
                            p = 0
                            while p < len(provinces):
                                if provco == provinces[p]["Code"]:
                                    c = 0
                                    while c < len(provinces[p]["Cantons"]):
                                        if cantco == provinces[p]["Cantons"][c]["Number"]:
                                            d = 0
                                            while d < len(provinces[p]["Cantons"][c]["Districts"]):
                                                if distco == provinces[p]["Cantons"][c]["Districts"][d]["Number"]:
                                                    disdel = provinces[p]["Cantons"][c]["Districts"][d]
                                                    delname = provinces[p]["Cantons"][c]["Districts"][d]["Name"]
                                                    provinces[p]["Cantons"][c]["Districts"].remove(disdel)
                                                    print("The district of " + delname + ", from the canton of " +
                                                          provinces[p]["Cantons"][c]["Name"] +
                                                          ", in the province of " + provinces[p][
                                                              "Name"] + ", has been deleted.")
                                                d += 1
                                        c += 1
                                p += 1
                        else:
                            print("Invalid disctict number, reinsert data.")
                            deldis()
                else:
                    print("Invalid canton number, reinsert data.")
                    deldis()
        else:
            print("Invalid province code, reinsert data.")
            deldis()


def delprov():  # This method deletes provices
    if len(provinces) == 0:
        print("No registered provinces have been found, you will be returned to the territorial distribution menu")
        menuprovin()
    else:
        for provin in provinces:
            print(provin["Name"] + ": " + provin["Code"])
        provco = input("Select a province to delete: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            i = 0
            while i < len(provinces):
                if provco == provinces[i]["Code"]:
                    provdel = provinces[i]
                    delname = provinces[i]["Name"]
                    provinces.remove(provdel)
                    print("The province of " + delname + " has been deleted.")
                i += 1
        else:
            print("Invalid province code, reinsert data.")
            delprov()


def delcan():  # This method allows to delete canton.
    if len(provinces) == 0:
        print("No registered provinces have been found, you will be redirected to the territorial distribution menu")
        menuprovin()
    else:
        for provin in provinces:
            print(provin["Name"] + ": " + provin["Code"])
        provco = input("Select the province the canton belongs to: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            if len(provinces[int(provco) - 1]["Cantons"]) == 0:
                print(
                    "No registered cantons have been found in this province, you will be returned to territorial distribution menu meu")
                menuprovin()
            else:
                for cant in provinces[int(provco) - 1]["Cantons"]:
                    print(cant["Name"] + ": " + cant["Number"])
                cantco = input("Select the canton you want to delete")
                if cantco.isdecimal() and int(cantco) in range(1, len(provinces[int(provco) - 1]["Cantons"]) + 1):
                    p = 0
                    while p < len(provinces):
                        if provco == provinces[p]["Code"]:
                            c = 0
                            while c < len(provinces[p]["Cantons"]):
                                if cantco == provinces[p]["Cantons"][c]["Number"]:
                                    candel = provinces[p]["Cantons"][c]
                                    delname = provinces[p]["Cantons"][c]["Name"]
                                    provinces[p]["Cantons"].remove(candel)
                                    print("The canton of " + delname + ", from the province of " + provinces[p][
                                        "Name"] + ", has been deleted.")
                                c += 1
                        p += 1
                else:
                    print("Invalid canton number, reinsert data.")
                    delcan()
        else:
            print("Invalid province code, reinser data.")
            delcan()


def menudel():  # This menu allows the user to delete either provinces, cantons or district
    print("1) Province.\n"
          "2) Canton.\n"
          "3) District.\n"
          "4) Back.")
    choi6 = input("Select and option: ")
    if choi6 == "1":
        print("You have chosen to delete a province.")
        delprov()
        menuprovin()
    elif choi6 == "2":
        print("You have chosen to delete a canton.")
        delcan()
        menuprovin()
    elif choi6 == "3":
        print("You have chosen to delete a district.")
        deldis()
        menuprovin()
    elif choi6 == "4":
        print("You have chosen to go back.")
        menuprovin()
    else:
        print("Invalid option, please select a valid one")
        menudel()


def moddis():  # This menu allows to modify districts
    if len(provinces) == 0:
        print("No registered provinces have been found, you will be redirected to the territorial distribution menu.")
        menuprovin()
    else:
        for provin in provinces:
            print(provin["Name"] + ": " + provin["Code"])
        provco = input("Select a province: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            if len(provinces[int(provco) - 1]["Cantons"]) == 0:
                print(
                    "No regisered cantons have been found in this province, you will be redirected to the territorial distribution menu.")
                menuprovin()
            else:
                for cant in provinces[int(provco) - 1]["Cantons"]:
                    print(cant["Name"] + ": " + cant["Number"])
                cantco = input("Select a canton: ")
                if cantco.isdecimal() and int(cantco) in range(1, len(provinces[int(provco) - 1]["Cantons"]) + 1):
                    if len(provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"]) == 0:
                        print(
                            "No registered districts have been found in this canton, you will be redirected to the territorial distribution menu")
                        menuprovin()
                    else:
                        for dist in provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"]:
                            print(dist["Name"] + ": " + dist["Number"])
                        distco = input("Select a district")
                        if distco.isdecimal() and int(distco) in range(1, len(
                                provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"]) + 1):
                            oldname = \
                            provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"][int(distco) - 1][
                                "Name"]
                            newname = input("Determine the new name of the district: ")
                            if newname.upper() in usednames:
                                print("Name already taken, reinsert data.")
                                moddis()
                            else:
                                provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]["Districts"][int(distco) - 1][
                                    "Name"] = newname
                                newnamed = newname.upper()
                                oldnamed = oldname.upper()
                                usednames.append(newnamed)
                                usednames.remove(oldnamed)
                                print("The district of " + oldname + ", in the canton of " +
                                      provinces[int(provco) - 1]["Cantons"][int(cantco) - 1]
                                      ["Name"] + ", located in the province of " + provinces[int(provco) - 1]["Name"] +
                                      ", has been changed to " + newname + ".")
                        else:
                            print("Invalid district number, reinsert data.")
                            moddis()
                else:
                    print("Invalid canton number, reinsert data.")
                    moddis()
        else:
            print("Invalid province code, reinsert data.")
            moddis()


def modcan():  # This menu allows to modify cantons
    if len(provinces) == 0:
        print("No registered provinces have been found. You will be redirected to de territorial distribution menu.")
        menuprovin()
    else:
        for provin in provinces:
            print(provin["Name"] + ": " + provin["Code"])
        provco = input("Province code: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            pp = 0
            while pp < len(provinces):
                if provco == provinces[pp]["Code"]:
                    if len(provinces[pp]["Cantons"]) == 0:
                        print(
                            "No registered cantons have been found in this province, you will be returned to the territorial distribution menu")
                        menuprovin()
                    else:
                        for canto in provinces[pp]["Cantons"]:
                            print(canto["Name"] + ": " + canto["Number"])
                        cantoco = input("Enter canton code: ")
                        if cantoco.isdecimal() and int(cantoco) in range(1, len(
                                provinces[int(provco) - 1]["Cantons"]) + 1):
                            newname = input("Enter the new name for the canton: ")
                            if newname.upper() in usednames:
                                print("Name already taken, reinser data.")
                                modcan()
                            else:
                                p = 0
                                while p < len(provinces):
                                    if provco == provinces[p]["Code"]:
                                        ppp = 0
                                        while ppp < len(provinces[p]["Cantons"]):
                                            if cantoco == provinces[p]["Cantons"][ppp]["Number"]:
                                                oldname = provinces[p]["Cantons"][ppp]["Name"]
                                                oldnamed = oldname.upper()
                                                usednames.remove(oldnamed)
                                                provinces[p]["Cantons"][ppp]["Name"] = newname
                                                newnamed = newname.upper()
                                                usednames.append(newnamed)
                                                print("The canton of", oldname, "has been changed to", newname)
                                                break
                                            ppp += 1
                                    p += 1
                else:
                    print("Invalid canton number, reinsert data.")
                    modcan()
                pp += 1
        else:
            print("Invalid canton code, reinsert data.")
            modcan()


def modprov():  # This menu allows to modify provinces
    if len(provinces) == 0:
        print("No registered provinces have been found. You will be redirected to de province creations menu.")
        menuprovin()
    else:
        for provin in provinces:
            print(provin["Name"] + ": " + provin["Code"])
        provco = input("Province code: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            newname = input("Input the new name of the province: ")
            if newname.upper() in usednames:
                print("Name already taken, reinsert data.")
                modprov()
            else:
                newdepu = input("Determine the new amount of deputies the province is allowed to have: ")
                if newdepu.isdigit():
                    p = 0
                    while p < len(provinces):
                        if provco == provinces[p]["Code"]:
                            oldname = provinces[p]["Name"]
                            oldnamed = oldname.upper()
                            usednames.remove(oldnamed)
                            newnamed = newname.upper()
                            usednames.append(newnamed)
                            olddepu = provinces[p]["Deputies"]
                            provinces[p]["Name"] = newname
                            provinces[p]["Deputies"] = newdepu
                            print("The province of", oldname, "has been change to", newname + ".",
                                  "Its number of deputies went from", olddepu, "to", newdepu + ".")
                        p += 1
                else:
                    print("Invalid amount of deputies, reinsert data.")
                    modprov()
        else:
            print("Invalid province code, reinsert data.")
            modprov()


def creadis():  # This menu allows to create districts
    if len(provinces) == 0:
        print("No registered provinces have been found. You will be redirected to de territorial distribution menu.")
        menuprovin()
    else:
        print("Enter the district's information as it is asked.")
        for provin in provinces:
            print(provin["Name"] + ": " + provin["Code"])
        provco = input("Province code: ")
        if provco.isdecimal() and int(provco) in range(1, len(provinces) + 1):
            pp = 0
            while pp < len(provinces):
                if provco == provinces[pp]["Code"]:
                    if len(provinces[pp]["Cantons"]) == 0:
                        print("No registered cantons have been found in this province."
                              " You will be redirected to the territorial distribution menu.")
                        menuprovin()
                    else:
                        for canto in provinces[pp]["Cantons"]:
                            print(canto["Name"] + ": " + canto["Number"])
                    cantoco = input("Enter canton code: ")
                    if cantoco.isdecimal() and int(cantoco) in range(1, len(provinces[int(provco) - 1]["Cantons"]) + 1):
                        num = str(len(provinces[int(provco) - 1]["Cantons"][int(cantoco) - 1]["Districts"]) + 1)
                        name = input("Enter the district's name: ")
                        if name.upper() in usednames:
                            print("Name already taken, reinsert data.")
                            creadis()
                        else:
                            distri = {"Number": num, "Name": name, "PresBall": [], "LegBall": []}
                            p = 0
                            while p < len(provinces):
                                if provco == provinces[p]["Code"]:
                                    ppp = 0
                                    while ppp < len(provinces[p]["Cantons"]):
                                        if provinces[p]["Cantons"][ppp]["Number"] == cantoco:
                                            provinces[p]["Cantons"][ppp]["Districts"].append(distri)
                                            named = name.upper()
                                            usednames.append(named)
                                            print("The district of " + distri[
                                                "Name"] + " has been successfully added to the canton of " +
                                                  provinces[p]["Cantons"][ppp]["Name"] + ","
                                                                                         " in the province of " +
                                                  provinces[p]["Name"] + ".")
                                        ppp += 1
                                p += 1
                    else:
                        print("Invalid canton number, reinsert data.")
                        creadis()
                pp += 1
        else:
            print("Invalid province code, reinsert data.")
            creadis()


def creacant():  # This menu allows to create cantons
    if len(provinces) == 0:
        print("No registered provinces have been found. You will be redirected to de territorial distribution menu.")
        menuprovin()
    else:
        print("Enter the canton's information as it is asked")
        for provin in provinces:
            print(provin["Name"] + ": " + provin["Code"])
        prov = input("Province code: ")
        if prov.isdecimal() and int(prov) in range(1, len(provinces) + 1):
            num = str(len(provinces[int(prov) - 1]["Cantons"]) + 1)
            nameca = input("Name: ")
            if nameca.upper() in usednames:
                print("Name already taken, reinsert data.")
                creacant()
            else:
                dist = []
                cant = {"Number": num, "Name": nameca, "Districts": dist, "PresBall": [], "LegBall": []}
                p = 0
                while p < len(provinces):
                    if prov == provinces[p]["Code"]:
                        provinces[p]["Cantons"].append(cant)
                        named = nameca.upper()
                        usednames.append(named)
                        print("The canton of " + cant["Name"] + " has been successfully added to the province",
                              provinces[p]["Name"] + ".")
                    p += 1
        else:
            print("Invalid province code, reinsert data.")
            creacant()


def creaprov():  # This menu allows to create provinces
    print("Please enter the province's data as it is asked:")
    code = str(len(provinces) + 1)
    namepr = input("Name: ")
    if namepr.upper() in usednames:
        print("Name already taken, reinsert data.")
        creaprov()
    else:
        dipu = input("Number or deputies: ")
        if dipu.isdigit():
            cants = []
            ballots = []
            provin = {"Code": code, "Name": namepr, "Deputies": dipu, "Cantons": cants, "PresBall": ballots,
                      "LegBall": ballots,
                      "Coeficient": 0, "Subcoeficient": 0}
            provinces.append(provin)
            named = namepr.upper()
            usednames.append(named)
            print("The province of " + provin["Name"] + " has been successfully created.")
        else:
            print("Invalid amount of deputies, reinsert data.")
            creaprov()


def menucre():  # This menu asks the user which type of territory they want to create
    print("1) Province.\n"
          "2) Canton.\n"
          "3) District.\n"
          "4) Back.")
    choi4 = input("Select an option: ")
    if choi4 == "1":
        print("You have chosen to create a province.")
        creaprov()

        menuprovin()
    elif choi4 == "2":
        print("You have chosen to create a canton.")
        creacant()
        menuprovin()
    elif choi4 == "3":
        print("You have chosen to create a district.")
        creadis()
        menuprovin()
    elif choi4 == "4":
        print("You have chosen to go to the previous menu.")
        menuprovin()
    else:
        print("You have chosen an invalid, please try again.")
        menucre()


def menumod():  # This menu asks the user which type of territory they want to modify
    print("1) Province.\n"
          "2) Canton.\n"
          "3) District.\n"
          "4) Back.")
    choi5 = input("Select territory type: ")
    if choi5 == "1":
        print("You have chosen to modify an existing province.")
        modprov()
        menuprovin()
    elif choi5 == "2":
        print("You have chosen to modify an existing canton.")
        modcan()
        menuprovin()
    elif choi5 == "3":
        print("You have chosen to modify an existing district.")
        moddis()
        menuprovin()
    elif choi5 == "4":
        print("You have chosen to exit the territory modification menu.")
        menuprovin()
    else:
        print("Invalid choice, please select a vaid option.")
        menumod()


def menuprovin():  # This menu shows the user the submenus contained within the tierritorial distribution menu
    print("1) Create.\n"
          "2) Modify.\n"
          "3) Delete\n"
          "4) Back")
    choi3 = input("Please select a submenu: ")
    if choi3 == "1":
        print("You have chosen to create the a new province, canton or district.\n"
              "Which of the three do you want to create?")
        menucre()
    elif choi3 == "2":
        print("You have chosen to modify an already existing provinces, cantos or districts.\n"
              "Select the type of territory that you want to modify.")
        menumod()
    elif choi3 == "3":
        print("You have chosen to delete one of the existing provinces, cantons or districts.")
        menudel()
    elif choi3 == "4":
        print("You have chosen to go to the previous menu.")
        menuadmin()
    else:
        print("Invalid choice, please select a valid menu.")
        menuprovin()


def menuadmin():  # This is the menu related to the administrator users
    print("1) Territorial distribution.\n"
          "2) Politic parties management.\n"
          "3) Ballots management.\n"
          "4) Electoral results.\n"
          "5) Consultations.\n"
          "6) Exit")
    choi2 = input("Select menu: ")
    if choi2 == "1":
        print("You have chosen the Territorial Distribution menu.\n"
              "Within this menu you will find options to create, modify and delete provinces, cantons and districts.")
        menuprovin()
    elif choi2 == "2":
        print("You have chosen the Political parties menu.\n"
              "In here, you will be able to create, modify and delete political parties.")
        menupart()
    elif choi2 == "3":
        print("You have chosen the Ballots menu.\n"
              "Here you can create, modify and delete ballots.")
        menuball()
    elif choi2 == "4":
        print("Here you can modify the results of the elections.")
        menuResults()
    elif choi2 == "5":
        print("Here you can do various consultations.")
        calculator()
    elif choi2 == "6":
        print("You have chosen to exit the current session.")
        menulogin()
    else:
        print("Invalid input, please choose a valid option.")
        menuadmin()


def menuguest():  # This menu is what users see hen they log in as a guest
    print("As a guest, you only have access to the Consultations function.")
    menucon()


def register():  # This menu is used to creater new accounts
    print("Enter the type of account: ")
    type = input("Admin(1) or Guest?(2): ")
    if type.isdecimal() and int(type) in range(1, 3):
        print("Enter you personal information as it is asked.")
        name = input("Full name: ")
        age = input("Age:")
        mail = input("E-mail: ")
        ID = input("ID: ")
        if ID in usednames:
            print("ID already taken, reinsert data")
            register()
        else:
            pawo = input("Password: ")
            newacc = {"Name": name, "Age": age, "E-mail": mail, "ID": ID, "Password": pawo, "Type": type}
            usednames.append(ID)
            accounts.append(newacc)
            print("Registration complete.")
    else:
        print("Invalid account type, reinsert data.")
        register()


def login():  # This menu is used by users to log in
    if len(accounts) == 0:
        print("No registered accounts have been found, you will be redirected to the registration menu.")
        menulogin()
    else:
        id = input("ID: ")
        pasw = input("Password: ")
        i = 0
        while i < len(accounts):
            if id == accounts[i]["ID"] and pasw == accounts[i]["Password"]:
                print("Welcome", accounts[i]["Name"] + ".")
                if accounts[i]["Type"] == "1":
                    print("You have logged in as an administrator\n"
                          "As an administrator ypu have access to the following options:")
                    menuadmin()
                    break
                elif accounts[i]["Type"] == "2":
                    print("You have logged in as a guest")
                    menuguest()
                    break
            i += 1
        else:
            print("No matching account has been found, please try again")
            login()


def menulogin():  # This is the first menu, asking users if the wanto to log in or register
    print("Press 1 if you want to log in. \n"
          "Press 2 if you want to register.")
    choi1 = input("Please select an option: ")
    if choi1 == "1":
        print("Now enter your ID and password.")
        login()

    elif choi1 == "2":
        register()
        menulogin()
    else:
        print("Invalid choice, please select a valid option")
        menulogin()


print("Welcome, please log in. If you do not have an account, please register.")
menulogin()
