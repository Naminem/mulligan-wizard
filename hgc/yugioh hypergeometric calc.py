from math import comb 

#int

A = int(input("Number of cards in deck: "))
B = int(input("Number of the cards you want in hand that's included in your deck: "))
C = int(input("Number of cards you currently have in hand: "))
D = int(input("Number of the cards you want in hand: "))

# removed A < x conditions, seems redundant

if D > B:
    print("\nYou can't have more copies of that card in hand. Try again.\n")
elif D > C:
    print("\nYou can't have more copies of that card than the amount of cards in your hand. Try again.\n")

# added cumulative so there's a clear cap to the calc even if realistically it won't get to that point

cumulative = 0.0

# comb(B, D) * comb(A - B, C - D) / comb(A, C) probably better

while True:
    E = comb(B, D) * comb(A - B, C - D)
    F = comb(A, C)
    frml = E / F * 100
    cumulative += frml
    
    if cumulative > 100:
        cumulative = 100.0

    print("\nProbability of hitting desired card(s) this draw:", round(frml, 2), "%")
    print("Probability of you drawing the desired card so far:", round(cumulative, 2), "%")
    print("Cards left in deck:", A - C)

#strip().lower() for broken caps
#isdigit() same thing but numbers -> error message

    cont = input("Add more draws? (y/n): ").strip().lower()
    if cont == "y":
        more = input("How many? ")
        if more.isdigit():
            C = C + int(more)

            while D > B or D > C:
                print("\nInvalid input after drawing:")
                if D > B:
                    print("- You can't draw more copies of the card than there are in the deck.")
                if D > C:
                    print("- You can't have more desired cards in hand than cards you've drawn.")

                #idk about the C value reinput for this but looks correct
                D = int(input("Re-enter the number of the cards you want in hand: "))
                C = int(input("Re-enter number of cards you currently have in hand: "))


        else:
            print("Please enter a number.")
    elif cont == "n":
        print("All set! It's time to deckbuild!")
        break
    else:
        print("Please type 'y' or 'n'.")

    # webbrowser.open() mdm/db deckbuilder but popus are annoying