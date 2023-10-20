col = 0
row = 0
basic.show_icon(IconNames.GHOST)

def on_forever():
    global row, col
    for index in range(4):
        if input.sound_level() == 128:
            row = randint(0, 4)
            col = randint(0, 4)
    if led.point(col, row):
        led.unplot(col, row)
        led.plot(col + 1, row)
basic.forever(on_forever)
