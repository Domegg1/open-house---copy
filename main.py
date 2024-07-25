R = 0
L = 0
while not (input.button_is_pressed(Button.A)):
    basic.show_arrow(ArrowNames.NORTH)
basic.pause(500)
basic.show_icon(IconNames.HEART)
basic.pause(500)
basic.show_icon(IconNames.HOUSE)
RefL = 2150

def on_forever():
    global L, R
    L = iBIT.read_adc(ibitReadADC.ADC1)
    R = iBIT.read_adc(ibitReadADC.ADC0)
    if L > RefL and R > RefL:
        iBIT.motor(ibitMotor.FORWARD, 25)
    elif L < RefL and R > RefL:
        iBIT.turn(ibitTurn.LEFT, 20)
    elif L > RefL and R < RefL:
        iBIT.turn(ibitTurn.RIGHT, 20)
    else:
        iBIT.motor_stop()
basic.forever(on_forever)
