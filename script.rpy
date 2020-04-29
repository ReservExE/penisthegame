label start:
    call default_room_objects_init
    jump game

label game:
    call clear_all_screens
    show screen main_room
    show screen main_room_menu
    "Что делаем сейчас"
    jump game




label clear_all_screens:
    hide screen main_room_menu
    hide screen main_room
    hide screen computer_menu
    return
