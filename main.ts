function A () {
    hola = "A"
}
input.onButtonPressed(Button.A, function () {
    hola = "XD"
})
input.onButtonPressed(Button.B, function () {
    A()
})
let hola = ""
hola = "hola"
while (true) {
    basic.showString(hola)
    basic.pause(1000)
}
