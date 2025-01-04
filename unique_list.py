def create_unique_list_and_calculate_average():
    """
    skapar en lista med unika element från användarinmatning 
    och beräknar genomsnittet av dessa.
    """

    print("skapa en lista med unika element.")
    unique_elements = set() # använder en mängd (set) för att lagra unika element. 

    while True:
        try:
            # tar in ett tal från användaren 
            user_input = input("ange ett tal (eller skriv 'klar' för att avsluta ): ").strip()
            
            if user_input.lower() == 'klar':
                break # avslutar om användaren skriver 'klar'

            # försöker konvertera inmatningen till ett flyttal (float)
            number = float(user_input)
            unique_elements.add(number) #lägger till talet i mängden
        except ValueError:
            print("ogiltig inmatning. ange ett giltigt tal eller 'klar'.")

        
