screen main_room():
    add default_room_OBJ.get_object_image()


screen main_room_menu():
    imagebutton: #bed
        xpos 0
        ypos 0
        focus_mask True
        idle default_bed_OBJ.get_object_image()
        hover default_bed_OBJ.get_hover_image()
        action [Jump("action_bed")]

    imagebutton: #computer
        xpos 0
        ypos 0
        focus_mask True
        idle default_computer_OBJ.get_object_image()
        hover default_computer_OBJ.get_hover_image()
        action [Jump("action_computer")]

    imagebutton: #mirror
        xpos 0
        ypos 0
        focus_mask True
        idle default_mirror_OBJ.get_object_image()
        hover default_mirror_OBJ.get_hover_image()
        action [Jump("action_mirror")]


screen computer_menu():
    imagemap:
        ground "images/menus/computer_menu.png"

        hotspot(445, 139, 227, 28):
            clicked Jump("action_cam")
            hovered ShowTransient("the_img", img="images/placeholders/PenisPC_cam_button.png")

        hotspot(446, 192, 225, 28):
            clicked Call("action_porn")
            hovered ShowTransient("the_img", img="images/placeholders/PenisPC_porno_button.png")

        hotspot(450, 252, 215, 27):
            clicked Call("action_shop")
            hovered ShowTransient("the_img", img="images/placeholders/PenisPC_shop_button.png")

screen the_img(img): #buttons handling
    add img pos (0, 0)
