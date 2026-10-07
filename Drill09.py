from pico2d import *

open_canvas(800, 600)

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

x = 400
y = 300

frame = 0

left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False

while True:
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
            exit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                left_pressed = True
            elif event.key == SDLK_RIGHT:
                right_pressed = True
            elif event.key == SDLK_UP:
                up_pressed = True
            elif event.key == SDLK_DOWN:
                down_pressed = True

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                left_pressed = False
            elif event.key == SDLK_RIGHT:
                right_pressed = False
            elif event.key == SDLK_UP:
                up_pressed = False
            elif event.key == SDLK_DOWN:
                down_pressed = False

    if right_pressed:
        x += 5

    if left_pressed:
        x -= 5

    if up_pressed:
        y += 5

    if down_pressed:
        y -= 5

    clear_canvas()

    ground.draw(400, 300, 800, 600)

    if right_pressed:
        character.clip_draw(
            1 + frame * 100, 101,
            100, 100,
            x, y,
            100, 100
        )

    elif left_pressed:
        character.clip_composite_draw(
            1 + frame * 100, 101,
            100, 100,
            0, 'h',
            x, y,
            100, 100
        )

    else:
        character.clip_draw(
            1 + frame * 100, 301,
            100, 100,
            x, y,
            100, 100
        )

    update_canvas()

    frame = (frame + 1) % 8
    delay(0.12)

close_canvas()