define s = Character('Серёга', color="#c8ffc8")
define l = Character("Лангепад", color="#e7e07d")
define m = Character("Миша", color="#ce7171")

init python:
    def csay(char, text, pause=0):
        if pause > 0:
            char(text, interact=False)
            renpy.pause(len(text)/20+pause)
        else:
            char(text, interact=True, ctc="ctc")

label start:
    call prologue

    return

label prologue:
    # jump startpos
    call at_home
    call bus_stop

    scene bg black
    with fade
    "Спустя одну не самую приятную поездку"
    call uni


    return

label at_home:
    scene bg room
    with fade

    $ csay(Character("Будильник"), "{i}*Дзынь-Дзынь*{/i}")

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
    scene bg stove
    with fade

    $ csay(Character("Яйца"), "{i}*Пшшшшш* *брызг* *брызг*{/i}", 1.0)
    $ csay(s, "Теперь можно и поесть наконец", 2.0)

    window hide
    scene bg black
    with fade

    "Спустя все утренние ритуалы..."

    return

label work_on_pc:
    return


label bus_stop:
    define b = Character("Бабка")

    scene bg bus_stop
    with fade

    $ csay(s, "Ненавижу ездить на автобусах", 2.0)
    $ csay(s, "И как я только выдержал эти четыре года утренних поездок в другой конец города?", 7.0)
    $ csay(s, "Хорошо, что больше мне не придётся с ними иметь дело", 1.0)
    $ csay(s, "Наверное")

    scene bg es_bus
    with dissolve

    $ csay(s, "О, почти пустой автобус.", 1.5)
    $ csay(s, "Жаль, что мне не по пути.")

    show babka 
    with dissolve

    $ csay(b, "Сынок, не подскажешь, который час?")

    $ csay(s, "{i}*Самое подходящее, чтобы этот автобус уже появился*{/i}", 4.0)
    $ csay(s, "Семь минут девятого, бабуль", 2.0)
    $ csay(s, "{i}*Как же она похожа на мою математичку, аж страшно{/i}")

    $ csay(b, "Спасибо, добрый человек")

    hide babka

    $ csay(s, "Да не за что", 1.5)
    $ csay(s, "{i}*Математичка — это последний человек, с которым я бы хотел встретиться сейчас{/i}", 6.0)
    $ csay(s, "{i}Никогда не любил ни её, ни то, что она преподаёт{/i}", 5.0)
    $ csay(s, "{i}Алгебра ещё куда ни шло,{/i}", 3.0)
    $ csay(s, "{i}а вот геометрия{/i}", 3.0)
    $ csay(s, "{i}Тупой предмет{/i}", 1.0)
    $ csay(s, "{i}столько нервов мне потратил!{/i}", 2.0)
    $ csay(s, "{i}Спасибо всевышнему, что мне больше не придется иметь с ней никаких дел*{/i}")

    scene bg bus
    with dissolve

    $ csay(s, "Вот и мой приехал", 2.0)
    $ csay(s, "Kак всегда забит")

    return

label uni:
    scene bg uni
    with fade 

    $ csay(s, "Ну, хоть доехал", 2.0)
    $ csay(s, "И на том спасибо", 3.0)
    $ csay(s, "...", 1.0)

    show langepad at midright
    with dissolve

    $ csay(s, "...", 1.0)

    show misha at midleft
    with dissolve

    $ csay(s, "О", 0.5)
    $ csay(s, "пацаны, привет", 0.5)
    $ csay(s, "как ощущения?")

    $ csay(l, "Привет, Серёга", 1.0)
    $ csay(l, "немного не то, что я ожидал", 4.0)
    $ csay(l, "как-то обыденно всё")

    $ csay(m, "А чего ты хотел?", 2.0)
    $ csay(m, "Чтобы лично президент прилетел поздравлять тебя?", 3.0)
    $ csay(m, "Или чтобы постелили тебе красную дорожку?")

    $ csay(l, "Не до такой степени, конечно", 3.0)
    $ csay(l, "но поторжественней что ли.", 2.0)
    $ csay(l, "В любом случае", 2.5)
    $ csay(l, "решили, что будете делать после уника?", 3.0)
    $ csay(l, "Лично я уже, считайте, устроенный", 3.0)
    $ csay(l, "меня ещё на стажировке отметили.", 3.0)
    $ csay(l, "В конторе сказали приходить работать после получения диплома.", 4.0)
    $ csay(l, "Видимо, тотальная нехватка кадров.")

    $ csay(m, "Повезло тебе.", 1.0)
    $ csay(m, "Я вот думаю попытаться устроиться в компанию, где работает мой брат", 6.0)
    $ csay(m, "может он замолвит за меня словечко.", 3.0)
    $ csay(m, "А ты как, Серёг?")

    $ csay(s, "Я пока не знаю", 1.0)
    $ csay(s, "думаю, сяду за фриланс.", 2.0)
    $ csay(s, "В общем, первое время буду плыть по течению, а там посмотрим.")

    $ csay(l, "Как обычно", 1.0)
    $ csay(l, "в твоём духе.")

    $ csay(m, "Кажется, начинается.", 1.0)
    $ csay(m, "Пошли уже к сцене")

    scene tribune
    with dissolve

    define prof = Character("Профессор")

    $ csay(prof, "Дорогие выпускники", 2.0)
    $ csay(prof, "С многими из вас сегодня мы прощаемся навсегда", 5.0)
    $ csay(prof, "На протяжении четырёх лет мы делали всё возможное, чтобы вы получили знания и навыки, которые могут пригодиться вам в вашем будущем пути.", 11.0)
    $ csay(prof, "Пользоваться ими или нет:", 3.0)
    $ csay(prof, "решать вам", 1.0)
    $ csay(prof, "Однако", 1.5)
    $ csay(prof, "я позволю себе дать вам совет", 3.0)
    $ csay(prof, "ни один специалист, каким бы квалифицированным он ни был, не стоит ничего, по сравнению с хорошо сплочённой командой. ", 9.0)
    $ csay(prof, "Учитесь ладить с людьми", 2.0)
    $ csay(prof, "это самый полезный навык, которому, к сожалению, нельзя обучить.", 6.0)
    $ csay(prof, "На этой ноте я удаляюсь.", 3.0)
    $ csay(prof, "Всем удачи, и прощайте!", 0.0)

    return


label ending_1_death_from_sugar:
    $ csay(s, "ой а у меня же диабет......", 2.0)

    window hide 
    scene bg black
    with fade
    pause

    "Серёга умер от передоза сахара в крови       // ну или что там у диабетиков"

    return





transform midright:
    xalign 0.7

transform midleft:
    xalign 0.3