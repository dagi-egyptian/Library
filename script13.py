book = {"Anan frank": 12 , "Diary of winpy kid": 24 , "The bourne identity": 16}
print("Menu")
print("A = Add a booK " , '\n', "B = Search for a book ",
      '\n', "C = View all book", '\n', "D = Update book data", '\n',
      "E = Remove a book ", '\n', "F = Borrow book ", '\n',
      "G = Return a book")
button = input(" choose a button? ")
if button == "A":
    book_name = input("Enter the book name? ")
    #You can't give the same code for different books
    Code = input("Enter a code for a book? ")
    print("successfully added!")
elif button == "B":
    n = input("Enter book's name? ")
    if n in book :
            print("book has found!")
            print("Code:", book[n])
    else:
            print("book hasn't found!")
            print("search for another book!")
elif button == "C":
    print("\n Name    : book code ")
    for key, value in book.items():
        print(key + ":" , value)
elif button == "D":
    d = input("Enter book's name? ")
    if d in book:
        A = input("Enter new book's name? ")
        book[d] = A
        print("Upgrade successful")
    else:
        print("invalid, try again")
elif button == "E":
    f = input("Enter a name of book you  want to remove: ")
    if f in book:
        book.pop(f)
        print("successfully removed")
    else:
        print("invalid")
elif button == "F":
    G = {"Anan frank": "available" ,
         "Diary of winpy kid": "borrowed" , "The bourne identity": "available"
         }
    h = input("choose a book: ")
    if G == "available":
        print("available")
    else:
        print("you have successfully borrowed it")
elif button == "G":
    i = {"Anan frank": "available" ,
         "Diary of winpy kid": "available" , "The bourne identity": "available"
         }
    h = input("choose a book: ")
    if i == "available":
        print("returned")
    else:
        print("you have successfully return it")
else:
    print("invalid button")