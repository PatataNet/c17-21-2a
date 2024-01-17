def A():
    global hola
    hola = "A"

def on_button_pressed_a():
    global hola
    hola = "XD"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    A()
input.on_button_pressed(Button.B, on_button_pressed_b)

hola = ""
hola = "hola"
while True:
    basic.show_string(hola)
    basic.pause(1000)