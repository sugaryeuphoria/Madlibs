def harryPotter():
    print("Welcome to Harry Potter and the Sorcerer's Stone Madlibs!")
    print("Let's create a magical story together.\n")

    character_name= input("Enter a character's Name: ")
    location=input("Enter a magical location: ")
    spell=input("Enter a magical spell: ")
    creature=input("Enter a magical creature: ")
    object_name=input("Enter a magical object: ")
    event=input("Enter the name of the magical event: ")

    story=(f"\nOnce upon a time, in the magical world of {location}, there lived a young wizard named {character_name}."
        f"\nOne day, while practicing {spell}, {character_name} encountered a friendly {creature}."
        f"\nThe {creature} led {character_name} to a hidden chamber where a powerful {object_name} was hidden."
        f"\nIntrigued by the discovery, {character_name} decided to use the {object_name} to attend the {event} that was happening in the wizarding world.")
    
    print(story)

harryPotter()    