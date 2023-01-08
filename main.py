from pyray import *
import classes
import scene_enum
import random
# Initalize window
init_window(500, 300, "DONKEY")
init_audio_device()
set_target_fps(120)
current_scene = 0
car = classes.Car(Vector2(0, 0))
donkey = classes.Donkey(Vector2(170, 0), 2)
road = load_texture("data/gfx/road.png")
bgcolor = (255, 255, 255)

explode = load_sound("data/sfx/explode.wav")
coin = load_sound("data/sfx/coin.wav")
score = 0
frame = 0
while not window_should_close():
    match current_scene:
        case scene_enum.TITLE:
            bgcolor = RAYWHITE
            if (is_mouse_button_released(0)):
                current_scene = scene_enum.GAME
        case scene_enum.GAME:
            bgcolor = (0, 171, 0)
            car.update()
            donkey.update()
            if (donkey.pos_vec.y > 400):
                play_sound(coin)
                score += 1
                donkey.pos_vec.y = -40
                donkey.pos_vec.x = random.choice([170, 270])
            if (check_collision_recs(car.collrec, donkey.collrec)):
                donkey.pos_vec = Vector2(random.choice([170, 270]), -40)
                score = 0
                current_scene = scene_enum.GAME_OVER
        case scene_enum.GAME_OVER:
            frame += 1
            bgcolor = (10, 10, 10)
            if (frame == 2):
                play_sound(explode)
            if (is_mouse_button_pressed(0)):
                frame = 0
                stop_sound(explode)
                current_scene = scene_enum.GAME
    begin_drawing()
    clear_background(bgcolor)
    match current_scene:
        case scene_enum.TITLE:
            draw_text("*************", 170, 100, 24, BLACK)
            draw_text("*   DONKEY  *", 170, 125, 24, BLACK)
            draw_text("*************", 170, 150, 24, BLACK)
            draw_text("Click to start!", 100, 200, 48, BLACK)
        case scene_enum.GAME:
            draw_text(str(score), 30, 30, 24, BLACK)
            draw_text("Space to\nswitch lanes", 10, 80, 24, BLACK)
            draw_texture_v(road, Vector2(340 - road.width, 0), WHITE)
            car.draw()
            donkey.draw()
        case scene_enum.GAME_OVER:
            draw_text("Game Over", 200, 150, 24, RAYWHITE)
            draw_text("Click to play again", 200, 200, 12, RAYWHITE)
    end_drawing()

close_window()