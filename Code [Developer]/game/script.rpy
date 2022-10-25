define s = Character('Серёга', color="#c8ffc8")

init python:
    def csay(char, text, pause=0):
        # TODO: показывать стпрелочку для продолжения диалога, если паузы нет
        char(text, interact=(pause == 0))
        if pause > 0:
            renpy.pause(len(text)/20+pause)

label start:
    call prologue

    return

label prologue:
    call at_home

    return

label at_home:
    scene bg room
    with fade

    "Будильник" "*Дзынь-Дзынь*"

    $ csay(s, "Мне определённо что-то снилось", 2.0)
    $ csay(s, "Но что...")

    $ csay(s, "Ну и ладно.", 1.0)
    $ csay(s, "...", 1.0)
    $ csay(s, "Такое странное ощущение…", 1.0)
    $ csay(s, "Сложно поверить, что это всё закончилось", 3.0)
    $ csay(s, "Моя главная мечта", 2.0)
    $ csay(s, "Цель последних двадцати двух лет моей жизни:", 3.0)
    $ csay(s, "Я выпускаюсь", 1.0)
    $ csay(s, "Теперь я сам себе хозяин")

    $ csay(s, "*Нюх-нюх*", 1.0)
    $ csay(s, "...", 1.0)
    $ csay(s, "Ничем не пахнет", 1.0)
    $ csay(s, "...", 1.0)
    $ csay(s, "Опять самому готовить")
    

    menu:
        "Пойти на кухню":
            call go_to_kitchen
        "Сесть за компьютер":
            call work_on_pc
    return


define has_tried_turning_on_gas = False
define has_picked_up_food = False

label go_to_kitchen:
    scene bg kitchen
    with fade

    if has_picked_up_food:
        menu:
            "Включить плиту":
                call eat_food
    elif not has_tried_turning_on_gas:
        menu:
            "Включить плиту":
                scene bg stove
                with fade

                $ csay(s, "Я, конечно, не в Европе, но просто так включать газ - плохая идея")

                $ has_tried_turning_on_gas = True
                jump go_to_kitchen

            "Открыть холодильник":
                call fridge
    else:
        menu:
            "Открыть холодильник":
                call fridge
    
    return

label fridge:
    scene bg fridge
    with fade

    $ csay(s, "Так, что мы имеем в нашем распоряжении?", 4.0)
    $ csay(s, "...", 1.0)
    $ csay(s, "Яйца и самый обычный йогурт", 3.0)
    $ csay(s, "...", 1.0)
    $ csay(s, "По крайней мере, хоть какой-то выбор имеется")
    menu:
        "Йогурт":
            jump ending_1_death_from_sugar
        "Яйца":
            $ csay(s, "Яйца, так яйца")
            $ has_picked_up_food = True
            jump go_to_kitchen


label eat_food:
    scene bg oven
    with fade

    $ csay(Character("Яйца"), "*Пшшшшш* *брызг* *брызг*", 1.0)
    $ csay(s, "Теперь можно и поесть наконец", 2.0)

    window hide
    scene bg black
    with fade

    "Спустя все утренние ритуалы..."

    return

label work_on_pc:
    return

label ending_1_death_from_sugar:
    $ csay(s, "ой а у меня же диабет......", 2.0)

    window hide 
    scene bg black
    with fade
    pause

    "Серёга умер от передоза сахара в крови       // ну или что там у диабетиков"

    return