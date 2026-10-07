from pico2d import *

open_canvas(800, 600)

ground = load_image('TUK_GROUND.png')

while True:
    clear_canvas()

    ground.draw(400, 300, 800, 600)

    update_canvas()

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()

close_canvas()