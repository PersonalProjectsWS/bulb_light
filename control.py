from yeelight import Bulb

bulb = Bulb('192.168.1.134')


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

while True:
    print("\nOpciones: ")
    print("Pulsa 1 para encender")
    print("Pulsa 2 para apagar")
    print("Pulsa 3 para verde")
    print("Pulsa 4 para rojo")
    option = str(input("\n¿que quieres hacer?"))

    if(option == "1"):
        bulb.turn_on()

    elif(option == "2"):
        bulb.set_default()
        bulb.turn_off()

    elif(option == "3"):
        bulb.set_rgb(56, 218, 73)

    elif(option == "4"):
        bulb.set_rgb(217, 54, 22)

    elif(option == "5"):
        bulb.set_brightness(10)

    elif(option == "6"):
        bulb.set_brightness(1000)

    elif(option == "7"): 
        bulb.effect = "sudden"


