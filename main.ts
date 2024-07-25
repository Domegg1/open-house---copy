let R = 0
let L = 0
while (!(input.buttonIsPressed(Button.A))) {
    basic.showArrow(ArrowNames.North)
}
basic.pause(500)
basic.showIcon(IconNames.Heart)
basic.pause(500)
basic.showIcon(IconNames.House)
let RefL = 2150
basic.forever(function () {
    L = iBIT.ReadADC(ibitReadADC.ADC1)
    R = iBIT.ReadADC(ibitReadADC.ADC0)
    if (L > RefL && R > RefL) {
        iBIT.Motor(ibitMotor.Forward, 25)
    } else if (L < RefL && R > RefL) {
        iBIT.Turn(ibitTurn.Left, 20)
    } else if (L > RefL && R < RefL) {
        iBIT.Turn(ibitTurn.Right, 20)
    } else {
        iBIT.MotorStop()
    }
})
