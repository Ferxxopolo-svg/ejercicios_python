def centrar(cad):
    for i in range(40 - (len(cad) // 2)):
        print(" ", end="")
    print(cad)
    for i  in range (40 - (len(cad) // 2)):
        print(" ", end="")
    for i in range(len(cad)):
        print("=", end="")
    print("")
message_1 = "Un Mensaje Centrado"
centrar(message_1)
message_2 = "Otro Mensaje"
centrar(message_2)