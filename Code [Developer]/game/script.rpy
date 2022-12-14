define s = Character('Серёга', color="#c8ffc8")
define p = Character('Паша', color="#667ec0")
define l = Character("Лангепад", color="#e7e07d")
define m = Character("Миша", color="#ce7171")
define zh = Character('Женя', color="#56bb6c")
define li = Character('Лиза', color="#00fff2")
define i = Character('Инвестор', color="#7e7e7e")

define relationship_w_teamlead = 0
define relationship_w_scriptwriter = 0
define relationship_w_coder = 0

define lied_about_math = True
define agreed_with_liza = True

init python:
    def csay(char, text, pause=0):
        if pause > 0:
            char(text, interact=False)
            renpy.pause(len(text)/20+pause)
        else:
            char(text, interact=True, ctc="ctc")

label start:
    call prologue from _call_prologue
    call first_day from _call_first_day
    call second_day from _call_second_day
    call third_day from _call_third_day
    call fourth_day from _call_fourth_day

    return

label prologue:
    call at_home from _call_at_home
    call bus_stop from _call_bus_stop

    scene bg black
    with fade
    "Спустя одну не самую приятную поездку"
    call uni from _call_uni

    return

label first_day:
    scene bg black
    with fade

    "На следующий день"

    scene bg room
    with fade

    $ csay(s, "Новый день опять настал, а смысл, меняется только дата в календаре,как день сурка, только хуже.", 1)
    $ csay(s, "Ты чувствуешь как твоё время истекает, снова я встану, снова поем, снова сяду за комп, снова лягу спать.", 1)
    $ csay(s, "Что ж, пора колесу сансары сделать новый оборот.")
    $ csay(s, "Как есть-то хочется...")

    scene bg kitchen
    with fade

    $ csay(s, "Ну ка-с, что там у нас есть из сьестного.")

    scene bg empty fridge
    with dissolve

    $ csay(s, "...", 1)
    $ csay(s, "...", 1)
    $ csay(s, "...", 1)
    $ csay(s, "Мда.... Надо идти за едой. Пожалуй, проверю перед уходом, что там нового в мире.")

    scene bg room
    with fade
    scene bg pc
    with fade

    play sound "<from 0 to 1>audio/vk.mp3"
    pause 2

    $ csay(s, "Интересно, кому я мог понадобиться.")
    $ csay(s, "Паша!? Давно с ним не общался, может взломали?")

    scene bg vk 1
    with dissolve

    $ csay(p, "{i}\"Привет, не хочешь встретиться?\"{/i}")

    $ csay(s, "Даже не знаю...")
    $ csay(s, "С одной стороны, вообще не хочу встречаться ни с кем из знакомых, с другой, хоть какое-то разнообразие.")

    scene bg vk 2
    with dissolve

    $ csay(p, "{i}\"Например через полчаса в какой-нибудь кафешке\"{/i}")

    $ csay(s, "Не готовить? Звучит заманчиво.")

    scene bg vk 3
    with dissolve

    $ csay(s, "{i}\"Давай, куда подходить?\"{/i}")

    scene bg vk 4
    with dissolve

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

    show pasha disappointed

    $ csay(p, "Всё настолько плохо?!")

    $ csay(s, "Ммм?")

    $ csay(p, "Да так...", 1)
    show pasha
    $ csay(p, "Я слышал ты до сих пор никуда не устроился, это правда?")

    $ csay(s, "А что, фриланс - это плохо?")

    $ csay(p, "А тебе нравится?")

    $ csay(s, "...", 1)
    $ csay(s, "Ну, да, я не работаю, к чему ты клонишь?")

    $ csay(p, "Мы с другом хотим основать свою игровую студию...")
    $ csay(p, "Студию - это громко сказано, команду. Я знаю, время не очень удачное для такого, но кто знает, может что и выйдет из этого. В общем, не хочешь ли присоединиться к нам?")

    $ csay(s, "Не очень удачное – это мягко сказано. Скорее совсем неподходящее. {i}*Хотя в этом даже есть что-то романтичное*{/i}")

    $ csay(p, "Дак что. Ты отказываешься?")
    
    $ csay(s, "Погоди! {i}*А, собственно, что я потеряю, если присоединюсь к ним, а так опыт получу*{/i} Пожалуй, я к вам примкну.")

    show pasha happy

    $ csay(p, "Отлично! Что думаешь на счёт того, чтобы посетить нашу студию?")

    $ csay(s, "Прям таки студию?")

    show pasha

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

            show pasha disappointed

            $ csay(p, "Какая есть. Видишь ли, мало кто хочет вкладываться в игровые компании в наше время. Если ты найдёшь нам инвестора, я буду очень благодарен. А пока, довольствуемся тем, что есть")
        "...":
            $ csay(s, "...")

    show pasha

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

    # menu:
    #     "Тимлид":
    #         call talk_to_teamlead
    #     "Сценарист":
    #         call talk_to_scriptwriter

    define talked_to_scriptwriter = False
    define talked_to_teamlead = False

    while not (talked_to_teamlead and talked_to_scriptwriter):
        if not talked_to_scriptwriter:
            show screen talk_to_scriptwriter_s
            with dissolve

        if not talked_to_teamlead:
            show screen talk_to_teamlead_s
            with dissolve

        hide pasha
        hide zhenya

        python:
            ui.interact()


    $ csay(s, "Понял, ну раз пока больше делать нечего, я пойду. Пока, парни.")

    $ csay(p, "Давай.")

    $ csay(zh, "Пока.")

    hide screen talk_to_scriptwriter_s
    hide talk_to_teamlead_s
    with dissolve

    scene bg outside
    with fade

    $ csay(s, "Удивительно, как может жизнь поменяться за один день. Кого-то сбивает машина, а меня вот пригласили в команду по разработке игр. Что вершит судьбу человека....")
    $ csay(s, "Когда я только начинал свой путь, я мечтал создавать игры, но с каждым годом, смотря новости, всё больше разочаровывался в них.")
    $ csay(s, "И вот, когда, казалось бы, индустрия лежит в гробу, находятся два человека, которые хватаются за лучик света, проникающий сквозь не до конца забитую крышку, и я, позабыв всё своё разочарование, следую за ними...")
    
    $ csay(s, "...", 1)
    $ csay(s, "...", 1)
    $ csay(s, "...", 1)

    $ csay(s, "Да, надо зайти в магазин. Умираю есть хочу.")

    if not lied_about_math:
        $ csay(s, "А, и ещё в библиотеку...", 1)
        $ csay(s, "Только я думал, что мои мучения окончены...")
        $ csay(s, "Ну что ж, значит я ошибался.")
        
    return

screen talk_to_teamlead_s:
    imagebutton:
        idle "pasha"
        action Call("talk_to_teamlead")
        at midright

screen talk_to_scriptwriter_s:
    imagebutton:
        idle "zhenya"
        action Call("talk_to_scriptwriter")
        at midleft

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

            show coder angry

            $ csay(Character('Незнакомка'), "Привет, Сергей.", 2)
            $ csay(Character('Незнакомка'), "А знаешь, родители хотели назвать меня Машей, но почему-то остановились на Елизавете.")

            $ csay(s, "Ой, прости пожалуйста. Просто я сейчас думал о Мише, и случайно спроектировал на тебя")

            show coder

            $ csay(li, "Так и быть, на первый раз прощаю.")

            menu:
                "\"А, знаешь, Маша тебе идёт\"":
                    $ relationship_w_coder -= 2

                    $ csay(s, "А, знаешь, Маша тебе идёт")

                    show coder angry

                    $ csay(li, "Я отказываюсь это комментировать")
                "\"Приятно видеть тебя вновь\"":
                    $ relationship_w_coder += 2

                    $ csay(s, "Приятно видеть тебя вновь. Мы, наверное, года 2 уже не виделись")

                    show coder happy

                    $ csay(li, "Взаимно. 2 года...", 1)
                    $ csay(li, "А кажется, что только месяц.")

        "\"Привет, а ты здесь какими судьбами?\"":
            $ csay(s, "Привет, а ты здесь какими судьбами?")

            $ csay(Character('Незнакомка'), "Да вот, вышла прогуляться с утреца. Жаль собаки нет, так бы каждый день это делала.")

            $ csay(s, "{i}Вспомнил, её Лиза зовут, это она всё хотела завести собаку, но никак не решалась{/i}")

    $ csay(s, "...", 1)
    $ csay(s, "Ну, как у тебя дела? Ты же тоже на кодера училась, где работаешь?")

    show coder upset

    $ csay(li, "Да как-то не очень, ушла недавно со стажировки в одной конторе неизвестной. Ужасное отношение, а требуют как с сеньёра. Сейчас сижу вот без работы. А у тебя как дела?")

    $ csay(s, "А я вот тоже безработным был до недавнего времени.", 1)
    $ csay(s, "{i}Да и сейчас не особо устроенный, что-то я сомневаюсь, что здесь будет постоянная ЗП{/i}", 1)
    $ csay(s, "Мой однокурсник хочет делать игры, ну вот и меня позвал.")

    show coder

    $ csay(li, "Серьёзно?! В такое-то время, ну он и отчаянный. И как успехи, когда выйдет игра?")

    $ csay(s, "По правде говоря, пока об этом рано говорить, у нас в команде и то пока только 3 человека.")

    $ csay(li, "Ааа, вот оно что.", 1)
    $ csay(li, "Хотя, звучит интересно. ....", 1)
    $ csay(li, "...", 1)
    $ csay(li, "А слушай, у вас в команде есть потребность в программисте? А то, я всё равно не работаю пока.")

    $ csay(s, "На самом деле, да. Нужен второй кодер, Паша довольно амбициозный, хочет собственный движок.")

    $ csay(li, "Паша?")

    $ csay(s, "Мой однокурсник.")

    show coder happy

    $ csay(li, "Хех, а я уж думала мир настолько тесен.", 1.5)
    show coder
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

            show pasha happy

            $ csay(p, "Оптимизм – это замечательно, однако лишние руки нам не помешают. Так что держи глаза открытыми.")

        "\"Я постараюсь найти кого-нибудь\"":
            $ csay(s, "Без геймдизайнера тяжеловато будет, я постараюсь найти кого-нибудь. Но ничего гарантировать не могу: большинство моих знакомых – кодеры.")

            $ csay(p, "Было бы замечательно, но если нет, то нет, надо уже браться за работу.")

    show pasha

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
            $ relationship_w_coder -= 1

            $ csay(s, "Будь здорова")

            show coder angry at midleft

            $ csay(li, "...", 1)
            $ csay(li, "Пожалуйста, не говори так.")

        "\"...\"":
            $ csay(s, "...")

    show coder at midleft

    $ csay(p, "...", 1)
    $ csay(p, "...", 1)
    $ csay(p, "Дороговато выйдет очиститель. Дороже, чем бюджет на разработку.")

    $ csay(li, "Найти бы спонсора нам.")

    show pasha angry at midright

    $ csay(p, "Нет! Принимать помощь от них – все равно что отказаться от своего видения продукта! Они всюду лезут, и хотят, чтобы было всё по их усмотрению.")

    menu:
        "\"Лиза права\"":
            $ csay(s, "Я согласен с Лизой, нам нужен спонсор, без него придётся туго.")

            $ csay(p, "Ага, отдаться ему с потрохами, а потом удивляться, почему игра отстой. Вот поэтому индустрия и в кризисе, из-за того, что маленькие студии продаются всяким “спонсорам”.")

            menu:
                "\"Не неси чепухи\"":
                    $ relationship_w_teamlead -= 1

                    $ csay(s, "Не неси чепухи.")

                    show pasha disappointed at midright

                    $ csay(p, "Эх, да что с вами спорить, ничего не понимаете.")
                
                "\"Подумай хорошенько\"":
                    $ relationship_w_teamlead += 2

                    $ csay(s, "А теперь подумай, вышли бы такие игры как “Халф лайф2”, “Гта 5”, “Варкрафт 3” и другие, без денежной поддержки?")

                    show pasha happy at midright

                    $ csay(p, "Пожалуй ты прав, я погорячился, спонсор – это не всегда зло.")

        "\"Паша прав\"":
            $ agreed_with_liza = False
            $ relationship_w_teamlead += 1

            $ csay(s, "Паша прав.", 1)
            $ csay(s, "{i}Зарплаты я не увижу...{/i}", 1)
            $ csay(s, "не нужны нам никакие инвесторы, мы и сами справимся.") 

            show pasha happy at midright

            $ csay(p, "Ты меня полностью понимаешь.")

            show coder angry at midleft

            $ csay(li, "Ну и ладно, делайте как знаете.")

    show pasha at midright
    show coder at midleft

    $ csay(li, "Делать больше нечего, так что я пойду. Пока парни.")

    $ csay(s, "Пока", 0.5)
    $ csay(p, "Пока")

    hide coder
    hide pasha
    show pasha
    with dissolve

    $ csay(s, "Ну тогда и я пойду, до встречи.")

    return

label no_investor_route:
    $ csay(s, "Не знаю, может зря мы отказываемся от финансовой помощи. Кто знает, далеко ли мы уедем на простом желании.", 1)
    $ csay(s, "Да и как раскручивать игру, надо либо огромные деньги в рекламную кампанию вкладывать, либо надеяться на чудо...")

    play sound "<from 0 to 4>audio/phone.mp3"
    pause 4 

    $ csay(Character("{i}Сообщение от Лизы{/i}"), "Привет, может всё-таки поговоришь с Пашей на счёт инвестора?", 1)
    $ csay(Character("{i}Сообщение от Лизы{/i}"), "А то я так размышляла, мы ж без денег загнёмся от голода просто. Тебе разве самому хочется бомжевать?")

    $ csay(s, "Хммм... Сложная ситуация. Надо обсудить с ней это.")

    menu:
        "\"Мы уже всё решили\"":
            $ relationship_w_coder -= 1

            $ csay(s, "Мы уже всё решили, поздно что-то менять")

            $ csay(li, "........... ой всё")

        "\"Я поговорю с ним\"":
            $ csay(s, "Я поговорю с ним, посмотрим, что можно сделать")

            $ csay(li, "Спасибо, я это ценю")

            $ csay(s, "Пожалуйста.")

    $ csay(s, "Надо позвонить Паше.")

    play sound "<from 2 to 4.5>audio/call.mp3"
    pause 3 

    $ csay(p, "Привет.")

    $ csay(s, "Привет.", 1)
    $ csay(s, "Я тут хотел поговорить на счёт инвестора, может всё-таки подумаешь на счёт него?")

    $ csay(p, "Ты говорил с Лизой?")

    $ csay(s, "Как ты узнал?")

    $ csay(p, "Догадался")

    menu:
        "Сдерзить":
            $ relationship_w_teamlead -= 1
            $ csay(s, "Ты, наверное, читаешь мысли {i}(Сарказм){/i}")

            $ csay(p, "Очень смешно.")

        "Сказать нормально":
            $ csay(s, "Да, она написала мне.")

            $ csay(p, "Ну подумай сам, игра уже наполовину готова.")

            $ csay(s, "Я о том же думаю.")

    $ csay(p, "В любом случае, поговори с Женей.")

    $ csay(s, "Да, точно, я забыл про него.", 1)
    $ csay(s, "Ну, до связи.")

    $ csay(p, "Досвидания")

    $ csay(s, "Ну, значит, надо поговорить с ним.")

    play sound "<from 2 to 4.5>audio/call.mp3"
    pause 3 

    $ csay(zh, "Привет, Серый, что хочешь?")

    $ csay(s, "Привет, а что ты думаешь на счёт инвестора?")

    $ csay(zh, "Что я думаю? Мне как-то без разницы. Что он есть, что его нет, мы всё равно сделаем крутую игру.")

    $ csay(s, "Ну ладно, оптимизм это хорошо. А я ем суфле птичка классическое.")

    $ csay(zh, "....................", 1)

    $ csay(zh, "Пока")
    
    play sound "<from 0 to 3>audio/endcall.mp3"
    pause 3.5

    $ csay(s, "Алё? Алё?")
    $ csay(s, "Доброе дело – правду говорить смело.")

    return

label investor_route:
    
    play sound "<from 0 to 4>audio/phone.mp3" volume 0.5
    pause 4 

    $ csay(s, "Алё")

    $ csay(p, "Твоё счастье, со мной связался один инвестор, некий форсен, хочет встретиться, я с ним не имею желания говорить, так что сходи ты.", 1)
    $ csay(p, "Можешь Лизу обрадовать")

    menu:
        "\"Да не злись ты так\"":
            $ csay(s, "Да не злись ты так, мы правда мало сможем чего добитсья без материальной помощи. Есть вещи превыше наших сил")

            $ csay(p, "И ты предпочёл даже не пытаться.", 1)
            $ csay(p, "Ну, будь по твоему.")

        "\"Я постараюсь добится свободы\"":
            $ relationship_w_teamlead += 2

            $ csay(s, "Я понимаю что ты не хочешь чтобы чьё-то постороннее мнение искажало авторский продукт.", 1)
            $ csay(s, "Но подумай, мы скорее всего ничего не сможем без посторонней помощи, но я постораюсь сделать всё возможное, чтобы не позволить чужому мнению видению влиять на нашу игру.")

            $ csay(p, "Скорее всего ты прав, прошу тебя только выбирай с умом.")

    $ csay(s, "Ну что ж, идём к вершителю судеб нашей компании.")

    scene bg cafe
    with fade

    show investor
    with dissolve

    $ csay(i, "Здравствуйте, вы должно быть Сергей.")

    $ csay(s, "Так и есть")

    $ csay(i, "Перейдём сразу к делу, подобного опыта у меня раньше не было, но я решил попытать удачу.", 1)
    $ csay(i, "Как вы понимаете, вкладываться в большие или средние студии бессмысленно, так что мой вгляд пал на маленькие команды энтузиастов, которых, на удивление оказалось мало.", 1)
    $ csay(i, "В вас я нахожу наибольший потенциал. Я готов вложить приличные деньги в разработку, но мне нужно, чтобы продукт был готов к определённому сроку, если игра выйдет успешной, то можно будет поговорить об увелечении штата.")

    $ csay(s, "А что на счёт автороского видения, будете ли вы подвергать его цензуре, если, например, посчитаете, что это пойдёт продажам на пользу?")

    $ csay(i, "Знаете, я думаю, что именно бесконечная цензура в угоду лучшим квартальным отчётам и привела индустрию в то место, где она сейчас пребывает.", 1)
    $ csay(i, "Так что я даю определённую свободу, в рамках закона, разумеется.")

    $ csay(s, "Спасибо вам огромное, мы это ценим. А когда приступим к совместной работе?")

    $ csay(i, "Сначала вам надо оформится с юридической точки зрения, насколько я знаю, вы, Сергей, не главный в команде.", 1)
    $ csay(i, "Я свяжусь с вашем тимлидом и сообщу всю информацию, а пока я вам предоставлю офис, можете переносить туда всё необходимо оборудование.")

    $ csay(s, "Раз всё решено, до скорого свидания, приятно иметь с вами дело")

    $ csay(i, "Взаимно")

    hide investor
    scene bg studio
    show coder at midleftplus
    show zhenya at midrightplus
    show pasha
    with fade

    $ csay(li, "Ну как всё прошло")

    $ csay(s, "Я бы сказал замечательно, сказал переезжать в новый офис. Сказал, что даёт нам творческую свободу. Так что можешь быть спокоен, Паша.")

    $ csay(p, "Не стал бы слепо доверять, но как ты говоришь, альтернатив у нас нет.")

    $ csay(li, "Про новый оффис это замечательно, надеюсь там есть воздушный фильтр.")

    show zhenya disappointed at midrightplus

    $ csay(zh, "И графические планшеты, тяжко без них.")

    $ csay(s, "А, и я так понял, что наш текущий состав остаётся пока без изменений. Так, что живём без геймдизайнера. Женя, надеюсь, ты сможешь нарисовать арты.")

    $ csay(zh, "Постараюсь, в художку я ходил, но это было давно и неправда")

    menu:
        "\"Постарайся, нужно произвести впечатление\"":
            $ relationship_w_scriptwriter -= 1

            show zhenya angry at midrightplus

            $ csay(s, "Постарайся, нам нужно произвести впечатление на нашего нового инвестора.")

            $ csay(zh, "Ничего обещать не могу, если б ему это было важно, мог бы и предоставить нам дизайнера.")

        "\"Делай как видишь\"":
            $ relationship_w_scriptwriter += 1

            $ csay(s, "Делай как видишь, главное сохрани свой стиль.")

            $ csay(p, "Да, кому как не сценаристу, лучше других знать как должна выглядеть игра.")

            show zhenya at midrightplus

            $ csay(zh, "Согласен, так я смогу полностью реализовать себя как автора.")

    show zhenya at midrightplus

    $ csay(p, "Тогда, ребята, пакуйте вещи, а я пошёл оформлять нас оффицально")

    hide coder
    hide pasha
    hide zhenya
    with dissolve
    
    return
    return

label third_day:
    scene bg black
    with fade
    "На следующий день..."
    scene bg park
    with fade

    $ csay(s, "Паша однозначно прав, издатель в угоду прибыли будет заставлять авторов изменять своему видению игры.", 1)
    $ csay(s, "С другой стороны права и Лиза, что может сделать одинокий инди разработчик, если не счастливая случайность никто не узнает про нашу игру....")

    if not agreed_with_liza:
        call no_investor_route from _call_no_investor_route
    else:
        call investor_route from _call_investor_route

    return

label fourth_day:
    scene bg black
    with fade
    "Несколько дней спустя"

    scene bg office
    with fade

    $ csay(s, "Надо поговорить с ребятами, а то в последние дни я заработался, что не знаю игра вообще разрабатывается или нет")

    define talked_to_zhenya = False
    define talked_to_pasha = False
    define talked_to_liza = False

    while not (talked_to_pasha and talked_to_zhenya and talked_to_liza):
        if not talked_to_pasha:
            show screen talk_to_pasha_s
            with dissolve

        if not talked_to_zhenya:
            show screen talk_to_zhenya_s
            with dissolve

        if not talked_to_liza:
            show screen talk_to_liza_s
            with dissolve

        hide pasha
        hide zhenya
        hide coder

        python:
            ui.interact()

    hide pasha
    hide zhenya
    hide coder
    show screen monitor_s
    with dissolve
    python:
        ui.interact()

    scene bg black
    with fade

    "Спасибо за игру"

    return

label ending:
    hide screen monitor_s
    scene bg black
    with fade

    "В таком ключе проходят последующие дни. Однако всему наступает свой черёд, так и *игра нейм* пора увидеть свет"

    call choose_ending

    return

screen monitor_s:
    imagebutton:
        idle "monitor idle"
        hover "monitor hover"
        action Call("ending")
        at monitorpos

transform monitorpos:
    xalign 0.475
    yalign 0.75

label choose_ending:
    define rc = relationship_w_coder
    define rt = relationship_w_teamlead
    define rs = relationship_w_scriptwriter

    call preending

    if not agreed_with_liza and (rc < 0 and rt < 0 and rs < 0):
        call ending1
    elif rt == 0 and rc < 0 and rs == 0:
        call ending211
    elif rt == 0 and rs < 0 and rc == 0:
        call ending212
    elif rt == 0 and rs > 0 and rc < 0:
        call ending221
    elif rt == 0 and rs < 0 and rc > 0:
        call ending222
    elif rt > 0 and rc < 0 and rs == 0:
        call ending231
    elif rt > 0 and rs < 0 and rc == 0:
        call ending232
    elif rt > 0 and rs > 0 and rc < 0:
        call ending241
    elif rt > 0 and rs < 0 and rc > 0:
        call ending242    
    elif not agreed_with_liza and rc == 0 and rt == 0 and rs == 0:
        call ending25
    elif not agreed_with_liza and ((rc > 0 and rt > 0) or (rt > 0 and rs > 0) or (rc > 0 and rs > 0)):
        call ending26
    elif rt < 0:
        call ending411
    elif rc > 0 and rs < 0:
        call ending412
    elif rc < 0:
        call ending413
    elif rs < 0:
        call ending414
    elif rc == 0 and rs == 0 and rt == 0:
        call ending42
    elif (rc > 0 and rt > 0) or (rt > 0 and rs > 0) or (rc > 0 and rs > 0):
        call ending43

    $ renpy.pause(2, hard=True)
    return

label preending:
    scene bg black
    with fade

    $ renpy.pause(1, hard=True)
    "Конец"
    $ renpy.pause(1, hard=True)

    return

label ending411:
    scene ending411
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша игра ушла в производственный ад, ты покинул команду"
    return

label ending412:
    scene ending412
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша игра не произвела никакого эффекта. Команду решену распустить"
    return

label ending413:
    scene ending413
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша игра не произвела никакого эффекта. Команду решену распустить"
    return

label ending414:
    scene ending414
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша игра не произвела никакого эффекта. Команду решену распустить"
    return

label ending42:
    scene ending42
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша игра не произвела ожидаемого эффекта, но решено сохранить команду и продолжить работу"
    return

label ending43:
    scene ending43
    with fade
    $ renpy.pause(2, hard=True)
    "Живительный свет вашей игры вернул веру в геймдев, команду решено сохранить и расширить"
    return

label ending1:
    scene ending1
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша команда распалась так и не выпустив игру, индустрия продолжает пребывать в кризисе"
    return

label ending211:
    scene ending1
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша команда распалась, лучик надежды мелькнул для индустрии... и погас"
    return

label ending212:
    scene ending1
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша команда распалась, лучик надежды мелькнул для индустрии... и погас"
    return

label ending221:
    scene ending221241
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша команда распалась, но ваш релиз вернул веру в геймдев, ты продолжишь работать в нём"
    return

label ending222:
    scene ending222242
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша команда сохранилась, но понесла потери в виде сценариста, вы продолжите работать над новыми проектами без сюжета"
    return

label ending231:
    scene ending1
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша команда сохраняется, несмоторя на полный провал игры"
    return

label ending232:
    scene ending1
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша команда сохраняется, несмоторя на полный провал игры"
    return

label ending241:
    scene ending221241
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша команда сохраняется. Ваш релиз вернул веру в геймдев, вы продолжаете работу над новыми проектами"
    return

label ending242:
    scene ending222242
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша команда сохраняется. Ваш релиз вернул веру в геймдев, вы продолжаете работу над новыми проектами"
    return

label ending25:
    scene ending25
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша игра была встречена нейтрально, вы абсолютно не представляете, что делать дальше"
    return

label ending26:
    scene ending26
    with fade
    $ renpy.pause(2, hard=True)
    "Ваша игра перевернула представление об играх. Вы продолжите работать над новыми проектами, но уже в расширенном составе и со славой"
    return

screen talk_to_pasha_s:
    imagebutton:
        idle "pasha"
        action Call("talk_to_pasha")
        at center

screen talk_to_zhenya_s:
    imagebutton:
        idle "zhenya"
        action Call("talk_to_zhenya")
        at midrightplus

screen talk_to_liza_s:
    imagebutton:
        idle "coder"
        action Call("talk_to_liza")
        at midleftplus

label talk_to_zhenya:
    hide screen talk_to_liza_s
    hide screen talk_to_pasha_s
    hide screen talk_to_zhenya_s 

    show zhenya
    with dissolve

    $ csay(s, "Привет Жень, как у тебя дела продвигаются со сценарием")

    show zhenya disappointed

    $ csay(zh, "Привет, да как-то не очень. Понимаешь вдохновения нет, а ты знаешь без него никуда.", 1)
    $ csay(zh, "Сижу уж который день в творческом кризисе, вроде мир стройный получается, но вот конфликт никак не могу придумать, одна банальщина выходит.")

    menu:
        "\"Аппетит приходит во время еды\"":
            $ relationship_w_scriptwriter += 1

            $ csay(s, "Аппетит приходит во время еды...", 1)
            $ csay(s, "Начни писать то, что выходит, хоть самую банальную банальщину. Посмотри на неё, начни исправлять точечно: там добавь драмы, там добавь остроты сюжету.", 1)
            $ csay(s, "Делать до победного конца.")

            show zhenya

            $ csay(zh, "Ха-ха, конечно, завернул ты, но я понял, что ты имеешь ввиду.", 1)
            $ csay(zh, "В твоих словах есть смысл, буду двигаться в таком направлении, может и вправду захочу есть.")

            $ csay(s, "Всегда к твоим услугам.")

        "\"А почему бы тебе не сменить сферу деятельности\"":
            $ relationship_w_scriptwriter -= 3

            $ csay(s, "А почему бы тебе не сменить поле деятельности, у нас как раз геймдизайнера нет.", 1)
            show zhenya angry
            $ csay(s, "...", 1)
            $ csay(s, "На время я имею ввиду... Я не предлагаю тебе полностью отказаться от написания сценариев...", 1)
            $ csay(s, "Просто если у тебя не получается сейчас может направить энергию в полезное русло... На пользу команды я имею ввиду.")

            $ csay(zh, "Я рассмотрю подобный вариант, надо только уведомить Пашу о кадровых перестановках")

            $ csay(s, "...")

        "\"Поднажми сроки горят\"":
            $ relationship_w_scriptwriter -= 1

            $ csay(s, "Поднажми, а то мы останемся без работы. Пойдёт и банальщина, всё лучше, чем отсутствие чего-либо в принципе.")

            show zhenya angry

            $ csay(zh, "Так-то оно так, ну ладно подкорректирую немного свои наработки и скину вам, авось потом придумаю что поинтереснее.")

            $ csay(s, "Время не терпит...")

    $ talked_to_zhenya = True

    hide zhenya 
    with dissolve

    return

label talk_to_pasha_no_investor:
    $ csay(s, "Привет.")

    $ csay(s, "Приви.")

    $ csay(s, "Слушай, напомни, зачем, нам свой собственный движок. Мы бы могли взять какой-нибудь юнити и не париться.")

    $ csay(p, "Собственый движок позволит нам быть независимыми, и мы сможем его оптимизировать под нашу игру.", 1)
    $ csay(p, "A то ты видел большинство инди-поделок, в них же играть можно только на суперкомпьютерах, тогда смысл нам тратить силы, если в нашу игру не смогут даже зайти?")

    menu:
        "\"Это проблемы игроков\"":
            $ relationship_w_teamlead -= 1

            $ csay(s, "Мне кажется, это проблемы игроков. Сейчас уже у всех есть компы сопоставимые по мощности с суперкомьютерами гугла.")

            show pasha angry

            $ csay(p, "Многие может и смогут запустить нашу игру, но у самой лояльной аудитории слабые компы, а нам нужны фанаты для будущих проектов.")

            $ csay(s, "Это закон такой?")

            $ csay(p, "Эмпирически выведеное правило.")

        "\"В твоих словах есть смысл\"":
            $ relationship_w_teamlead += 1

            $ csay(s, "В твоих словах есть смысл. Но всё равно, не много ли для первого проекта писать с нуля движок?")

            show pasha happy

            $ csay(p, "Рассматривай это как инвестицию в будущее. В будущем будет легче, ведь проще доработать, чем писать с нуля.", 1)
            $ csay(p, "Да и плюсом представь, как это будеть смотреться в твоём резюме.")

            $ csay(s, "Солидно.")

            $ csay(p, "Вот и я о том же.", 1)
            $ csay(p, "Ничего, поднажми ещё немного, скоро мы станем знамениты.")

            $ csay(s, "Да я и без славы обойтись могу, в принципе")

    return

label talk_to_pasha:
    hide screen talk_to_liza_s
    hide screen talk_to_pasha_s
    hide screen talk_to_zhenya_s

    $ talked_to_pasha = True

    show pasha
    with dissolve

    if not agreed_with_liza:
        call talk_to_pasha_no_investor from _call_talk_to_pasha_no_investor
        hide pasha
        with dissolve
        return

    $ csay(s, "Привет Паш, как оценишь состояние проекта, всё нормально? В сроки укладываемся?")

    $ csay(p, "Привет, да вроде всё выглядит нормально, идёт, но...")

    show pasha disappointed

    $ csay(s, "Но?")

    $ csay(p, "Но, мне не даёт покоя наша сделка с тем инвестором. Да, он держит обещание и не вмешивается, но это пока мы никому неизвестны.", 1)
    $ csay(p, "А вот представь, мы выпускаем игру, она становится популярной, теперь у публики есть ожидания от нас.", 1)
    $ csay(p, "A он ведь хочет видеть результат своих вложений, так что он начнёт давить на нас, чтобы оправдать ожидания людей, наймёт студию аналитики.", 1)
    $ csay(p, "И ВСЁ! Наш продукт в заложниках.")

    menu:
        "\"А где минусы\"":
            $ relationship_w_teamlead -= 2

            $ csay(s, "А где минусы?", 1)
            show pasha angry
            $ csay(s, "Не, я понимаю свобода самовыражения и всё такое, но подумай какие зарплаты он нам будет платить, обернись наша игра успехом. Разве эта пресловутая свобода стоит тех денег?")

            $ csay(p, "Вот из-за мыслящих так как ты индустрия и скатилась.", 1)
            $ csay(s, "Вы смотрите только на краткосрочную выгоду, в погоне на прибыль вы забываете о долгоиграющих последствиях, хотя эти самые последствия ведут к потерям не только лично вашим, но и общечеловеческим.")

            $ csay(s, "Лично я, могу просто пойти работать кодером в другую сферу. Да и все мы.")

            $ csay(p, "В нашем мире все сферы взаимосвязаны, кризис в одной неизбежно повлечёт кризис в другой, хотя это может быть не так очевидно.")

            $ csay(s, "...")

            $ csay(p, "Ой, да что с вами говорить, с самого начала всё понятно было.")

        "\"Всегда можно уйти\"":
            $ relationship_w_teamlead += 1

            $ csay(s, "Всегда можно уйти от него, мы же не подписывались на постоянное сотрудничество.")

            show pasha disappointed

            $ csay(p, "Но компания-то ему принадлежать будет.")

            $ csay(s, "Главное не название, а люди что за этим названием стоят, мы можем основать новую компанию, благо деньги у нас будут.", 1)
            $ csay(s, "A если их будет мало, можно организовать краудфандинговую компанию, что-то типа “Новый проект от людей, подаривших вам *Игра нейм*”")

            show pasha happy

            $ csay(p, "Ну кстати да, я как-то не подумал о краудфандинге. Спасибо, что разубедил в обречённости нашего будущего.")

            $ csay(s, "Всегда к твоим услугам.")

    hide pasha
    with dissolve

    return

label talk_to_liza_no_investor:
    $ csay(li, "Привет.")

    $ csay(s, "Привет.")

    $ csay(li, "Слушай, на счёт инвестора. Вот он говорит, что это убивает творческое начало, свободу самовыражения.")

    $ csay(s, "Что-то подобное я от него слышал.")

    $ csay(li, "Ну вот, в Америке до принятия антимонопольных законов, кинотеатры могли позволить себе снимать эпические картины с огромным размахом.", 1)
    $ csay(li, "После их принятия, все эпические полотна пропали, зато появились всякие дешёвые блокбастеры.")

    $ csay(li, "Это я к тому, что финансовая помощь позволяет авторам создавать нечто великое, то, на что, у простого творца попросту не хватит средств.", 1)
    $ csay(li, "Недостаток средств намного больше ограничивает свободу автора, чем какие-то абстрактные спонсоры.")

    menu:
        "\"Я не думал под этим углом\"":
            $ relationship_w_coder += 1

            $ csay(s, "Я не думал под этим углом. Тут и вправду есть смысл.")

            show coder happy

            $ csay(li, "Вот видишь, инвестор мог быть и не плохой идеей.")
            $ csay(li, "Но уже поздно что-либо менять...")

            $ csay(s, "Не поспоришь. Доделаем игру и посмотрим как пойдёт.")

        "\"Тебе так кажется\"":
            $ relationship_w_coder -= 2

            $ csay(s, "Тебе так кажется.")

            show coder angry

            $ csay(li, "Почему?")

            $ csay(s, "Автор сможет донести посыл с любыми средствами, даже пещерные люди это могли. А вот когда тебе стоит, по сути, запрет на донесение мыслей, сделать это гораздо сложнее.")

            $ csay(li, "Видимо, тут где-то излучатель стоит...")

            $ csay(s, "Что?")

            $ csay(li, "Забей.")


    return

label talk_to_liza:
    hide screen talk_to_liza_s
    hide screen talk_to_pasha_s
    hide screen talk_to_zhenya_s

    $ talked_to_liza = True

    show coder
    with dissolve

    if not agreed_with_liza:
        call talk_to_liza_no_investor from _call_talk_to_liza_no_investor
        hide coder
        with dissolve
        return

    $ csay(li, "Привет. Вот скажи мне почему мы должны писать движок с нуля, почему не использовать готовый, даже есть из чего выбирать.", 1)
    $ csay(li, "Написание с нуля столько времени отнимает, мы бы уже готовый продукт выпустили, если б не заморочки с движком.")

    menu:
        "\"Рассматривай это как проверку своих возможностей\"":
            $ relationship_w_coder += 1

            $ csay(s, "И тебе привет. Ну ты можешь рассматривать это как проверку своих сколов, написание движка явно задача неординарная.")

            show coder upset

            $ csay(li, "Я как-то уверена в своих сколах. Не думаю, что они нуждаются в проверке")

            $ csay(s, "Ну может быть ты и уверена, а вот работодатель не всегда. А если у тебя в резюме будет значиться движок, написанный с нуля, он сразу поймёт с кем имеет дело.")

            show coder

            $ csay(li, "В чём-то ты прав, наверное. Ну ладно, но я всё равно поговорю с Пашей.")

            $ csay(s, "Всегда к твоим услугам.")

        "\"Так сказало начальство\"":
            $ relationship_w_coder -= 1

            $ csay(s, "Так сказал начальник, ему виднее.")

            show coder upset

            $ csay(li, "И тебя ничего не тревожит. Например, что мы можем не уложиться в сроки?")

            $ csay(s, "Наверное, раз он поставил такую задачу, он распланировал так, чтобы учитывать время на разработку движка.")

            $ csay(li, "...", 1)
            $ csay(li, "Начальство всегда право значит. Ну и ладно, значит и ответственность за сгоревшие дедлайны ложится на него.")

            $ csay(s, "Всегда к твоим услугам.")

        "\"А почему бы тебе не спросить у тимлида\"":
            $ relationship_w_coder -= 1
            $ relationship_w_teamlead -= 1

            show coder upset

            $ csay(s, "А почему бы тебе не поговорить с тимлидом?")

            $ csay(li, "Может потому, что это я выдвинула идею об инвесторе, которая, как ты знаешь, немного так не понравилась.")

            $ csay(s, "И всё же я не вижу причин тебе не поговорить с ним. Не будешь же ты не вступать с ним в контакт до конца разработки.")

            $ csay(li, "Хочешь остаться ни при делах, а самому то тоже неохота писать. Ну ладно я поговорю с ним.")

            $ csay(s, "Всегда к твоим услугам.")

    hide coder
    with dissolve

    return

label talk_to_teamlead:
    hide screen talk_to_scriptwriter_s
    hide screen talk_to_teamlead_s

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

    $ talked_to_teamlead = True

    hide pasha
    with dissolve

    return

label talk_to_scriptwriter:
    hide screen talk_to_scriptwriter_s
    hide screen talk_to_teamlead_s

    show zhenya
    with dissolve

    $ csay(s, "А что, у нас уже есть готовый сценарий?")

    $ csay(zh, "Пока есть только набор идей, но их надо обсуждать с геймдизайнером, его, как видишь, нет. Но мне уже они нравятся. Рассказать тебе?")

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
            show zhenya
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

                    show zhenya disappointed

                    $ csay(s, "Такое ощущение, что я уже слышал это, и, причём, не один раз. Думаю, нам нужно что-то пооригинальнее.")

                    $ csay(zh, "Повторюсь, это только идеи, до конечного продукта ещё далеко. Да и ты думаешь так просто придумать что-то оригинальное? Куча всего уже было придуманно до нас. Мы не живём не в каменном веке, где любая идея была новой. Нам остаётся только что и переваривать уже имеющиеся идеи.")

                    $ csay(s, "Ладно, не я сценарист, не мне об этом думать.")

    $ talked_to_scriptwriter = True

    hide zhenya
    with dissolve

    return

screen choose_pc:
    imagebutton:
        auto "choose pc %s"
        action Call("work_on_pc")
        at pc
        
transform pc:
    xalign 0.16
    yalign 0.48

screen choose_door:
    imagebutton:
        auto "choose door %s"
        action Call("go_to_kitchen")
        at door

transform door:
    xalign 0.385
    yalign 0.4


label at_home:
    scene bg room
    with fade

    play sound "audio/alarm.mp3" volume 0.5

    $ csay(Character("Будильник"), "{i}*Дзынь-Дзынь*{/i}")

    $ csay(s, "Мне определённо что-то снилось, но что...")

    $ csay(s, "Ну и ладно.", 1.0)
    $ csay(s, "...", 1.0)
    $ csay(s, "Такое странное ощущение…, cложно поверить, что это всё закончилось.", 1.5)
    $ csay(s, "Моя главная мечта, цель последних двадцати двух лет моей жизни: я выпускаюсь, теперь я сам себе хозяин")

    $ csay(s, "*Нюх-нюх*", 1.0)
    $ csay(s, "...", 1.0)
    $ csay(s, "Ничем не пахнет", 1.0)
    $ csay(s, "...", 1.0)
    $ csay(s, "Опять самому готовить...")

    show screen choose_pc
    show screen choose_door
    with dissolve

    python:
        ui.interact()

    return

label choose_stove:
    hide screen choose_fridge
    hide screen choose_stove_1st_time
    hide screen choose_stove_2nd_time

    scene bg stove
    with fade

    $ csay(s, "Я, конечно, не в Европе, но просто так включать газ - плохая идея")

    $ has_tried_turning_on_gas = True
    jump go_to_kitchen
    return

screen choose_stove_1st_time:
    imagebutton:
        auto "choose stove %s"
        action Call("choose_stove")
        at stovepos

screen choose_stove_2nd_time:
    imagebutton:
        auto "choose stove %s"
        action Call("eat_food")
        at stovepos

transform stovepos:
    xalign 0.59
    yalign 0.999

transform fridgepos:
    xalign 0.03
    yalign 0.999

screen choose_fridge:
    imagebutton:
        auto "choose fridge %s"
        action Call("fridge")
        at fridgepos

define has_tried_turning_on_gas = False
define has_picked_up_food = False
define chose_eggs = False

label go_to_kitchen:
    hide screen choose_door
    hide screen choose_pc
    hide screen choose_eggs_s
    hide screen choose_yoghurt_s

    scene bg kitchen
    with fade
    
    if has_picked_up_food and chose_eggs:
        show screen choose_stove_2nd_time
        with dissolve

    elif has_picked_up_food and not chose_eggs:
        pause 1.5
        $ csay(s, "Вкусный")
        $ csay(s, "Я бы ещё чего-нибудь съел, но пора идти.")

        window hide
        scene bg black
        with fade

        "Спустя все утренние ритуалы..."

        return

    elif not has_tried_turning_on_gas:
        show screen choose_stove_1st_time
        show screen choose_fridge
        with dissolve
    
    else:
        show screen choose_fridge
        with dissolve

    python:
        ui.interact()

    return

transform yoghurtpos:
    xalign 0.37
    yalign 0.5

transform eggspos:
    xalign 0.45
    yalign 0.93

screen choose_yoghurt_s:
    imagebutton:
        hover "yoghurt hover.png"
        idle "yoghurt idle.png"
        action Call("choose_yoghurt")
        at yoghurtpos

screen choose_eggs_s:
    imagebutton:
        hover "eggs hover.png"
        idle "eggs idle.png"
        action Jump("choose_eggs")
        at eggspos

label fridge:
    hide screen choose_stove_1st_time
    hide screen choose_stove_2nd_time
    hide screen choose_fridge 

    image yoghurt = "yoghurt idle.png"
    image eggs = "eggs idle.png"

    scene bg empty fridge
    show yoghurt at yoghurtpos
    show eggs at eggspos
    with fade

    $ csay(s, "Так, что мы имеем в нашем распоряжении?")
    $ csay(s, "Яйца и самый обычный йогурт")
    $ csay(s, "По крайней мере, хоть какой-то выбор имеется")
    
    show screen choose_eggs_s
    show screen choose_yoghurt_s

    python:
        ui.interact()

    return

label choose_yoghurt:
    hide screen choose_eggs_s
    hide screen choose_yoghurt_s
    $ csay(s, "Йогурт, так йогурт")
    $ has_picked_up_food = True
    jump go_to_kitchen

    return
            

label choose_eggs:
    hide screen choose_eggs_s
    hide screen choose_yoghurt_s
    $ chose_eggs = True
    $ csay(s, "Яйца, так яйца")
    $ has_picked_up_food = True
    jump go_to_kitchen

    return


label eat_food:
    hide screen choose_stove_1st_time
    hide screen choose_stove_2nd_time
    hide screen choose_fridge
    if chose_eggs:
        scene bg stove
        with fade

        $ csay(Character("Яйца"), "{i}*Пшшшшш* *брызг* *брызг*{/i}")

    $ csay(s, "Теперь можно и поесть наконец")

    window hide
    scene bg black
    with fade

    "Спустя все утренние ритуалы..."

    return

label work_on_pc:
    hide screen choose_door
    hide screen choose_pc

    scene bg pc
    with fade

    $ csay(s, "...")
    call go_to_kitchen from _call_go_to_kitchen
    return


label bus_stop:
    define b = Character("Бабка")

    scene bg bus_stop
    with fade

    $ csay(s, "Ненавижу ездить на автобусах", 1)
    $ csay(s, "И как я только выдержал эти четыре года утренних поездок в другой конец города?", 1)
    $ csay(s, "Хорошо, что больше мне не придётся с ними иметь дело", 1.0)
    $ csay(s, "Наверное")

    scene bg es_bus
    with dissolve

    $ csay(s, "О, почти пустой автобус.", 1.0)
    $ csay(s, "Жаль, что мне не по пути.")

    show babka 
    with dissolve

    $ csay(b, "Сынок, не подскажешь, который час?")

    $ csay(s, "{i}*Самое подходящее, чтобы этот автобус уже появился*{/i}", 1)
    $ csay(s, "Семь минут девятого, бабуль", 1)
    $ csay(s, "{i}*Как же она похожа на мою математичку, аж страшно{/i}")

    $ csay(b, "Спасибо, добрый человек")

    hide babka
    with dissolve

    $ csay(s, "Да не за что")
    $ csay(s, "{i}*Математичка — это последний человек, с которым я бы хотел встретиться сейчас{/i}", 1.0)
    $ csay(s, "{i}Никогда не любил ни её, ни то, что она преподаёт{/i}", 1.0)
    $ csay(s, "{i}Алгебра ещё куда ни шло, а вот геометрия...{/i}", 1.0)
    $ csay(s, "{i}Тупой предмет.{/i}", 1.0)
    $ csay(s, "{i}Cтолько нервов мне потратил!{/i}", 1.0)
    $ csay(s, "{i}Спасибо всевышнему, что мне больше не придется иметь с ней никаких дел*{/i}")

    scene bg bus
    with fade

    $ csay(s, "Вот и мой приехал. Kак всегда забит")

    return

label uni:
    scene bg uni
    with fade 

    $ csay(s, "Ну, хоть доехал. И на том спасибо")

    show langepad at midright
    with dissolve

    $ csay(s, "...", 1.0)

    show misha at midleft
    with dissolve

    $ csay(s, "О, пацаны, привет. Kак ощущения?")

    $ csay(l, "Привет, Серёга. Немного не то, что я ожидал, как-то обыденно всё")

    $ csay(m, "А чего ты хотел? Чтобы лично президент прилетел поздравлять тебя? Или чтобы постелили тебе красную дорожку?")

    $ csay(l, "Не до такой степени, конечно, но поторжественней что ли.")
    $ csay(l, "В любом случае, решили, что будете делать после уника?", 1)
    $ csay(l, "Лично я уже, считайте, устроенный, меня ещё на стажировке отметили. В конторе сказали приходить работать после получения диплома.", 1)
    $ csay(l, "Видимо, тотальная нехватка кадров.")

    $ csay(m, "Повезло тебе. Я вот думаю попытаться устроиться в компанию, где работает мой брат, может он замолвит за меня словечко.", 1)
    $ csay(m, "А ты как, Серёг?")

    $ csay(s, "Я пока не знаю, думаю, сяду за фриланс.", 1.0)
    $ csay(s, "В общем, первое время буду плыть по течению, а там посмотрим.")

    $ csay(l, "Как обычно, в твоём духе.")

    $ csay(m, "Кажется, начинается. Пошли уже к сцене")

    define prof = Character("Профессор")

    hide misha
    hide langepad
    with dissolve

    $ csay(prof, "Дорогие выпускники!")
    $ csay(prof, "Сo многими из вас сегодня мы прощаемся навсегда.")
    $ csay(prof, "На протяжении четырёх лет мы делали всё возможное, чтобы вы получили знания и навыки, которые могут пригодиться вам в вашем будущем пути.")
    $ csay(prof, "Пользоваться ими или нет, решать вам. Однако, я позволю себе дать вам совет", 1.0)
    $ csay(prof, "Hи один специалист, каким бы квалифицированным он ни был, не стоит ничего, по сравнению с хорошо сплочённой командой. ")
    $ csay(prof, "Учитесь ладить с людьми, это самый полезный навык, которому, к сожалению, нельзя обучить.")
    $ csay(prof, "На этой ноте я удаляюсь. Всем удачи, и прощайте!")

    return


label ending_1_death_from_sugar:
    $ csay(s, "ой а у меня же диабет......", 2.0)

    window hide 
    scene bg black
    with fade
    pause

    "Серёга умер от передоза сахара в крови       // ну или что там у диабетиков"

    return

transform center:
    xalign 0.5
    yalign 0.99

transform midright:
    xalign 0.7
    yalign 0.99

transform midrightplus:
    xalign 0.85
    yalign 0.99

transform midleft:
    xalign 0.3
    yalign 0.99

transform midleftplus:
    xalign 0.15
    yalign 0.99