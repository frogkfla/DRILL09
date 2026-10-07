from pico2d import *

open_canvas(800, 600)

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

x = 400
y = 300

frame = 0

while True:
    clear_canvas()

    ground.draw(400, 300, 800, 600)

    character.clip_draw(
        1 + frame * 100, 301,
        100, 100,
        x, y,
        100, 100
    )

    update_canvas()

    frame = (frame + 1) % 8
    delay(0.12)

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()

close_canvas()