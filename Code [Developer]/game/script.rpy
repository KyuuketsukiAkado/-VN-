﻿define s = Character('Серёга', color="#c8ffc8")
define p = Character('Паша', color="#667ec0")
define l = Character("Лангепад", color="#e7e07d")
define m = Character("Миша", color="#ce7171")
define zh = Character('Женя', color="#56bb6c")
define li = Character('Лиза', color="#00fff2")

define relationship_w_teamlead = 0
define relationship_w_scriptwriter = 0
define relationship_w_coder = 0

# TODO: Эмоции персов


define lied_about_math = True

init python:
    def csay(char, text, pause=0):
        if pause > 0:
            char(text, interact=False)
            renpy.pause(len(text)/20+pause)
        else:
            char(text, interact=True, ctc="ctc")

label start:
    # call start_pos

    call prologue
    call fisrt_day
# label start_pos:
    call second_day
    call third_day
    call fourth_day

    return

label prologue:
    call at_home
    call bus_stop

    scene bg black
    with fade
    "Спустя одну не самую приятную поездку"
    call uni


    return
# Ваще по красоте я считаю
label fisrt_day:
    scene bg room
    with fade

    $ csay(s, "Новый день опять настал, а смысл, меняется только дата в календаре,как день сурка, только хуже. Ты чувствуешь как твоё время истекает, снова я встану, снова поем, снова сяду за комп, снова лягу спать. Что ж, пора колесу сансары сделать новый оборот.")
    $ csay(s, "Как есть-то хочется...")

    scene bg kitchen
    with fade

    $ csay(s, "Ну ка-с, что там у нас есть из сьестного.")

    scene bg empty fridge
    with dissolve

    $ csay(s, "...", 1)
    $ csay(s, "...", 1)
    $ csay(s, "...", 1)
    $ csay(s, "Мда.... Надо идти за едой. Пожалуй, проверю, что там нового в мире.")

    scene bg room
    with fade
    scene bg pc
    with fade

    $ csay(Character('Вконтакте'), "{i}Звук уведомления{/i}")
    $ csay(s, "Интересно, кому я мог понадобиться.", 1)
    $ csay(s, "...", 1.0)
    $ csay(s, "Паша!? Давно с ним не общался, может взломали?")

    scene bg vk
    with dissolve

    $ csay(p, "{i}\"Привет, не хочешь встретиться?\"{/i}")

    $ csay(s, "Даже не знаю...", 1.0)
    $ csay(s, "...", 1.0)
    $ csay(s, "С одной стороны, вообще не хочу встречаться ни с кем из знакомых, с другой, хоть какое-то разнообразие.")

    $ csay(p, "{i}\"Например через полчаса в какой-нибудь кафешке\"{/i}")

    $ csay(s, "Не готовить?", 1.0)
    $ csay(s, "Звучит заманчиво.")

    $ csay(s, "{i}\"Давай, куда подходить?\"{/i}")

    $ csay(p, "{i}\"На Пушкина 49, “Голубая устрица”\"{/i}")

    scene bg black
    with fade
    "Через полчаса..."

    scene bg cafe
    with fade

    show pasha
    with dissolve

    $ csay(p, "Привет, серый. Давно не виделись.")

    $ csay(s, "Привет, да, давненько.", 1)
    $ csay(s, "...", 1)
    $ csay(s, "Как жизнь?")

    $ csay(p, "Да так, потихоньку", 1)
    $ csay(p, "...", 1)
    $ csay(p, "...")

    $ csay(Character('Оффициант'), "Ваш заказ.")

    $ csay(s, "{i}*Набрасывается на еду*{/i}")

    $ csay(p, "Всё настолько плохо?!")

    $ csay(s, "Ммм?")

    $ csay(p, "Да так...", 1)
    $ csay(p, "Я слышал ты до сих пор никуда не устроился, это правда?")

    $ csay(s, "А что, фриланс - это плохо?")

    $ csay(p, "А тебе нравится?")

    $ csay(s, "...", 1)
    $ csay(s, "Ну, да, я не работаю, к чему ты клонишь?")

    $ csay(p, "Мы с другом хотим основать свою игровую студию...", 2)
    $ csay(p, "Студию - это громко сказано, команду. Я знаю, время не очень удачное для такого, но кто знает, может что и выйдет из этого. В общем, не хочешь ли присоединиться к нам?")

    $ csay(s, "Не очень удачное – это мягко сказано. Скорее совсем неподходящее. {i}*Хотя в этом даже есть что-то романтичное*{/i}")

    $ csay(p, "Дак что. Ты отказываешься?")
    
    $ csay(s, "Погоди! {i}*А, собственно, что я потеряю, если присоединюсь к ним, а так опыт получу*{/i} Пожалуй, я к вам примкну.")

    $ csay(p, "Отлично! Что думаешь на счёт того, чтобы посетить нашу студию?")

    $ csay(s, "Прям таки студию?")

    $ csay(p, "Мою квартиру...")

    $ csay(s, "Что ж, пойдём.")

    hide pasha

    scene bg black
    with fade

    "В студии"

    scene bg studio
    with fade

    show pasha
    with dissolve

    $ csay(p, "Вот это наше рабочее место.")

    menu:
        "{i}\"Хорошая студия\"{/i}":
            $ relationship_w_teamlead -= 1

            $ csay(s, "Хорошая студия")

            $ csay(p, "Какая есть. Видишь ли, мало кто хочет вкладываться в игровые компании в наше время. Если ты найдёшь нам инвестора, я буду очень благодарен. А пока, довольствуемся тем, что есть")
        "...":
            "..."

    $ csay(Character('Незнакомец', color="#56bb6c"), "Что тут происходит?")

    $ csay(p, "Привет, Женя. Не думал, что ты сюда придёшь сегодня.")

    hide pasha
    show pasha at midright
    with dissolve
    show zhenya at midleft
    with dissolve

    $ csay(zh, "Хелло, да я тут вчера забыл наброски.", 1)
    $ csay(zh, "...", 1)
    $ csay(zh, "А тебя я не помню, ты кто?")
    
    $ csay(p, "Это наш новый кодер, Серёга, мой одногрупник.")
    $ csay(p, "А это наш сценарист, Женя, прошу любить и жаловать.")

    $ csay(s, "Приятно познакомится.")

    $ csay(zh, "Взаимно.")

    $ csay(p, "Пока осмотрись тут.")

    call look_around_the_studio    

    scene bg outside
    with fade

    $ csay(s, "Удивительно, как может жизнь поменяться за один день. Кого-то сбивает машина, а меня вот пригласили в команду по разработке игр. Что вершит судьбу человека....")
    $ csay(s, "Когда я только начинал свой путь, я мечтал создавать игры, но с каждым годом, смотря новости, всё больше разочаровывался в них. И вот, когда, казалось бы, индустрия лежит в гробу, находятся два человека, которые хватаются за лучик света, проникающий сквозь не до конца забитую крышку, и я, позабыв всё своё разочарование, следую за ними...")
    
    $ csay(s, "...", 1)
    $ csay(s, "...", 1)
    $ csay(s, "...", 1)

    $ csay(s, "Да, надо зайти в магазин. Умираю есть хочу.")

    if not lied_about_math:
        $ csay(s, "А, и ещё в библиотеку...", 1)
        $ csay(s, "Только я думал, что мои мучения окончены...", 1)
        $ csay(s, "Ну что ж, значит я ошибался.")
        
    return

label second_day:
    scene bg black
    with fade
    "На послеследующее утро"

    scene bg park
    with fade

    if lied_about_math:
        $ csay(s, "М-да, сфера видео всё больше деградирует. Авторы воруют друг у друга контент, мнения продаются и покупаются, монтаж становится всё более и более дёрганным.", 1)
        $ csay(s, "Скоро дойдёт до того, что дети просто не смогут концентрировать внимание хотя бы на секунду. Ну, хотя, ей всё рано не обогнать сферу игр, ведь те с первой космической проваливаются в бездну.")

        $ csay(s, "К слову о них, надо искать людей в команду. Кто у меня есть из знакомых...", 1.0)
    else:
        $ csay(s, "Дааа, давно я так мозги не напрягал. Надо сказать, у меня с математикой не всё так плохо: что-то да помню. Да и учебник Пашин хороший, понятнее чем в тех, по которым я учился...", 2.0)
        $ csay(s, "К слову о нём, сообщений от него не было с позавчера, видимо, никого не нашёл, этак мы далеко не уедем.")

        $ csay(s, "Надо самому вспоминать знакомых...", 1.0)

    $ csay(s, "...", 1)

    $ csay(s, "Я помню кто-то тоже хотел делать игры, но как же его звали...", 1.0)
    $ csay(s, "На М вроде,", 1.0)
    $ csay(s, "но ладно, если не помню, значит и не надо.")

    show coder silhouette small
    with dissolve

    $ csay(s, "...", 1)
    $ csay(s, "Кто-то тоже погулять с утра вышел...")
    $ csay(s, "Кого-то она мне напоминает.")

    hide coder silhouette small
    show coder 
    with dissolve

    $ csay(Character('Незнакомка'), "Привет, вот уж не ожидала тебя тут встретить.")

    $ csay(s, "{i}Ааааа!{/i}", 0.75)
    $ csay(s, "{i}Что делать?{/i}", 0.75)
    $ csay(s, "{i}Я не помню кто это.{/i}", 0.75)
    $ csay(s, "{i}Кто же, кто же...{/i}", 1.25)
    $ csay(s, "{i}А, вспомнил!{/i}", 1)
    $ csay(s, "{i}Эта та из старшей школы, которая ещё ненавидит, когда ей говорят будь здорова{/i}")

    menu:
        "\"Привет, Маш, давно не виделись\"":
            $ relationship_w_coder -= 1

            $ csay(s, "Привет, Маш, давно не виделись. Как жизнь?")

            $ csay(Character('Незнакомка'), "Привет, Сергей.", 2)
            $ csay(Character('Незнакомка'), "А знаешь, родители хотели назвать меня Машей, но почему-то остановились на Елизавете.")

            $ csay(s, "Ой, прости пожалуйста. Просто я сейчас думал о Мише, и случайно спроектировал на тебя")

            $ csay(li, "Так и быть, на первый раз прощаю.")

            menu:
                "\"А, знаешь, Маша тебе идёт\"":
                    $ relationship_w_coder -= 2

                    $ csay(s, "А, знаешь, Маша тебе идёт")

                    $ csay(li, "Я отказываюсь это комментировать")
                "\"Приятно видеть тебя вновь\"":
                    $ relationship_w_coder += 2

                    $ csay(s, "Приятно видеть тебя вновь. Мы, наверное, года 2 уже не виделись")

                    $ csay(li, "Взаимно. 2 года...", 1)
                    $ csay(li, "А кажется, что только месяц.")

        "\"Привет, а ты здесь какими судьбами?\"":
            $ csay(s, "Привет, а ты здесь какими судьбами?")

            $ csay(Character('Незнакомка'), "Да вот, вышла прогуляться с утреца. Жаль собаки нет, так бы каждый день это делала.")

            $ csay(s, "{i}Вспомнил, её Лиза зовут, это она всё хотела завести собаку, но никак не решалась{/i}")

    $ csay(s, "...", 1)
    $ csay(s, "Ну, как у тебя дела? Ты же тоже на кодера училась, где работаешь?")

    $ csay(li, "Да как-то не очень, ушла недавно со стажировки в одной конторе неизвестной. Ужасное отношение, а требуют как с сеньёра. Сейчас сижу вот без работы. А у тебя как дела?")

    $ csay(s, "А я вот тоже безработным был до недавнего времени.", 1)
    $ csay(s, "{i}Да и сейчас не особо устроенный, что-то я сомневаюсь, что здесь будет постоянная ЗП{/i}", 1)
    $ csay(s, "Мой однокурсник хочет делать игры, ну вот и меня позвал.")

    $ csay(li, "Серьёзно?! В такое-то время, ну он и отчаянный. И как успехи, когда выйдет игра?")

    $ csay(s, "По правде говоря, пока об этом рано говорить, у нас в команде и то пока только 3 человека.")

    $ csay(li, "Ааа, вот оно что.", 1)
    $ csay(li, "Хотя, звучит интересно. ....", 1)
    $ csay(li, "...", 1)
    $ csay(li, "А слушай, у вас в команде есть потребность в программисте? А то, я всё равно не работаю пока.")

    $ csay(s, "На самом деле, да. Нужен второй кодер, Паша довольно амбициозный, хочет собственный движок.")

    $ csay(li, "Паша?")

    $ csay(s, "Мой однокурсник.")

    $ csay(li, "Хех, а я уж думала мир настолько тесен.", 1.5)
    $ csay(li, "Ну что, мне надо проходить собеседование? Или главное в кодере его наличие?")

    $ csay(s, "На счёт собеседования не знаю, но вот познакомится с командой явно стоит. Пошли в нашу “студию”, я напишу Паше, чтоб готовил хлеб да соль.")

    hide coder
    show bg black
    with fade
    "В квартире"


    show bg studio
    show coder
    with fade 

    $ csay(s, "Вот мы и на месте.")

    hide coder
    show coder at midleft
    show pasha at midright
    with dissolve

    $ csay(p, "Привет, ты же Лиза, да?")

    $ csay(li, "Да, это – я. А ты, стало быть, Паша?")

    $ csay(p, "Приятно познакомиться. Проходи, поизучай нашу студию, пока работы нет.")

    hide coder
    hide pasha
    show pasha
    with dissolve

    $ csay(s, "Ну, как успехи в поисках геймдизайнера? Есть кто на примете?")

    $ csay(p, "Хотел то же самое спросить у тебя...", 1.5)
    $ csay(p, "Судя по всему, придётся мне исполнять его роль. Никто не хочет к нам идти. Даю срок ещё один день, если не найду никого, то я буду этим заниматься.")

    menu:
        "\"Я уверен, из тебя выйдет хороший геймдизайнер\"":
            $ relationship_w_teamlead += 1

            $ csay(s, "Я уверен, из тебя выйдет хороший геймдизайнер. Мы сможем и текущим составом состряпать шедевр.")

            $ csay(p, "Оптимизм – это замечательно, однако лишние руки нам не помешают. Так что держи глаза открытыми.")

        "\"Я постараюсь найти кого-нибудь\"":
            $ csay(s, "Без геймдизайнера тяжеловато будет, я постараюсь найти кого-нибудь. Но ничего гарантировать не могу: большинство моих знакомых – кодеры.")

            $ csay(p, "Было бы замечательно, но если нет, то нет, надо уже браться за работу.")

    $ csay(s, "А где Женя?")

    $ csay(p, "Он взял себе выходной.")

    $ csay(s, "Игры сложно писать, особенно когда не знаешь, что именно тебе надо писать.")

    $ csay(p, "Всё будет, пока и ты отдыхай. Через день, если не будет подходящих кандидатур, мы с ним встретимся , обсудим всё и скажем направление, в котором вам надо будет двигаться.")

    hide pasha
    show pasha at midright
    show coder at midleft
    with dissolve

    $ csay(li, "Апчхи...", 1)
    $ csay(li, "Как тут пыльно у вас, не помешало бы очиститель воздуха поставить.")

    menu:
        "\"Будь здорова\"":
            $ csay(s, "Будь здорова")

            $ csay(li, "...", 1)
            $ csay(li, "Пожалуйста, не говори так.")

        "\"...\"":
            $ csay(s, "...")

    $ csay(p, "...", 1)
    $ csay(p, "...", 1)
    $ csay(p, "Дороговато выйдет очиститель. Дороже, чем бюджет на разработку.")

    $ csay(li, "Найти бы спонсора нам.")

    $ csay(p, "Нет! Принимать помощь от них – все равно что отказаться от своего видения продукта! Они всюду лезут, и хотят, чтобы было всё по их усмотрению.")

    menu:
        "\"Лиза права\"":
            $ csay(s, "Я согласен с Лизой, нам нужен спонсор, без него придётся туго.")

            $ csay(p, "Ага, отдаться ему с потрохами, а потом удивляться, почему игра отстой. Вот поэтому индустрия и в кризисе, из-за того, что маленькие студии продаются всяким “спонсорам”.")

            menu:
                "\"Не неси чепухи\"":
                    $ relationship_w_teamlead -= 1

                    $ csay(s, "Не неси чепухи.")

                    $ csay(p, "Эх, да что с вами спорить, ничего не понимаете.")
                
                "\"Подумай хорошенько\"":
                    $ relationship_w_teamlead += 2

                    $ csay(s, "А теперь подумай, вышли бы такие игры как “Халф лайф2”, “Гта 5”, “Варкрафт 3” и другие, без денежной поддержки?")

                    $ csay(p, "Пожалуй ты прав, я погорячился, спонсор – это не всегда зло.")

        "\"Паша прав\"":
            $ relationship_w_teamlead += 1

            $ csay(s, "Паша прав.", 1)
            $ csay(s, "{i}Зарплаты я не увижу...{/i}", 1)
            $ csay(s, "не нужны нам никакие инвесторы, мы и сами справимся.") 

            $ csay(p, "Ты меня полностью понимаешь.")

            $ csay(li, "Ну и ладно, делайте как знаете.")

    $ csay(li, "Делать больше нечего, так что я пойду. Пока парни.")

    $ csay(s, "Пока", 0.5)
    $ csay(p, "Пока")

    hide coder
    hide pasha
    show pasha
    with dissolve

    $ csay(s, "Ну тогда и я пойду, до встречи.")

    return

label third_day:
    return

label fourth_day:
    return

label look_around_the_studio:
    # define curr_choice = 0
    # menu:
    #     "Тимлид":
    #         $ curr_choice = 2
    #     "Сценарист":
    #         $ curr_choice = 1

    # if curr_choice == 1:
    #     call talk_to_scriptwriter
    # else:
    #     call talk_to_teamlead

    menu:
        "Тимлид":
            call talk_to_teamlead
        "Сценарист":
            call talk_to_scriptwriter

    $ csay(s, "Понял, ну раз пока больше делать нечего, я пойду. Пока, парни.")

    $ csay(p, "Давай.")

    $ csay(zh, "Пока.")

    hide pasha
    with dissolve
    hide zhenya
    with dissolve

    return

label talk_to_teamlead:
    hide zhenya
    with dissolve
    hide pasha
    show pasha
    with dissolve

    $ csay(s, "Ну, вроде, я всё посмотрел, что тут есть. Какие задачи на меня возложены?")
    $ csay(p, "Для начала, я помню у тебя были проблемы с математикой. Я надеюсь, ты их решил, как кодеру она тебе понадобится.")

    menu:
        "Соврать":
            $ relationship_w_scriptwriter -= 1
            $ relationship_w_teamlead -= 1

            $ csay(s, "Да, я подтянул математику тогда, пришлось, к сожалению.")

            $ csay(p, "А я бы сказал к счастью, меньше работы сейчас делать.")

        "Сказать правду":
            $ lied_about_math = False
            $ csay(s, "Нет...", 1)
            $ csay(s, "И что мне теперь делать?")

            $ csay(p, "Печально, но нет ничего непоправимого. Я знаю один учебник, он мне помог подтянуть матешу в своё время, потом скину тебе его название, я его недавно видел в библиотеке неподалёку.")
            $ csay(p, "С первой задачей определились: подтянуть тебе математку.")

    $ csay(p, "...", 1)   
    $ csay(p, "...", 1)
    $ csay(p, "А, да. Я не хочу использовать готовые движки, поэтому будь готов писать с нуля, я сомневаюсь, что ты справишься в одиночку, поэтому советую тебе поискать кодера в напарники.")
    $ csay(p, "Также нам нужен геймдизайнер, если знаешь кого, дай мне знать. Пока задач больше нет, как только случатся подвижки, дам тебе знать.")

    return

label talk_to_scriptwriter:
    hide pasha 
    with dissolve
    hide zhenya
    show zhenya
    with dissolve

    $ csay(s, "А что, у нас уже есть готовый сценарий?")
    $ csay(s, "Пока есть только набор идей, но их надо обсуждать с геймдизайнером, его, как видишь, нет. Но мне уже они нравятся. Рассказать тебе?")

    menu:
        "Отказаться":
            $ csay(s, "Не, не надо. Не люблю спойлеры.")
            $ csay(zh, "Как знаешь, если передумаешь, напиши мне.")

        "Выслушать его":
            $ csay(s, "Давай, выкладывай, мне интересно.")
            $ csay(zh, "Если вкратце. Главная героиня живёт в неопостапокалиптическом мире, где цивилизация уже восстановилась после катастрофы....")

            scene bg black
            with fade
            "Спустя 5 минут"
            scene bg studio
            with fade
            
            $ csay(zh, "...И это всё является соцальным комментарием на тему, является ли наше общество цивилизацей.", 1)
            $ csay(zh, "...", 1)
            $ csay(zh, "Ну что думаешь?")

            menu:
                "Глубоко":
                    $ relationship_w_scriptwriter += 1

                    $ csay(s, "Да, я, конечно, половины не понял, но звучит, как что-то интересное. Не так много философских игр существует в мире, так что вполне вероятно, что игра возымеет успех.")

                    $ csay(zh, "Хех, надеюсь. Однако необходимо понимать, что не всякая идея подходит для воплощения в форме игры. Надо советоваться с геймдизайнером, так что может выйти так, что сценарий будет совсем не похож на только что рассказанное мной.")

                    $ csay(s, "В любом случае, мне кажется, у получится тебя что-нибудь да придумать.")

                    $ csay(zh, "Спасибо.")

                "Избито":
                    $ relationship_w_scriptwriter -= 1

                    $ csay(s, "Такое ощущение, что я уже слышал это, и, причём, не один раз. Думаю, нам нужно что-то пооригинальнее.")

                    $ csay(zh, "Повторюсь, это только идеи, до конечного продукта ещё далеко. Да и ты думаешь так просто придумать что-то оригинальное? Куча всего уже было придуманно до нас. Мы не живём не в каменном веке, где любая идея была новой. Нам остаётся только что и переваривать уже имеющиеся идеи.")

                    $ csay(s, "Ладно, не я сценарист, не мне об этом думать.")
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
    yalign 0.99

transform midleft:
    xalign 0.3
    yalign 0.99