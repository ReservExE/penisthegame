label default_room_objects_init:
        $ default_room_OBJ = room_object_class(object_image_name = "room_default", object_image_path = "images/rooms/",
                                     idle_image_name = "room_default", idle_image_path = "images/rooms/",
                                     hover_image_name = "room_default", hover_image_path= "images/rooms/")

        $ default_bed_OBJ = room_object_class(object_image_name = "bed_default", object_image_path = "images/beds/",
                                     idle_image_name = "bed_default", idle_image_path = "images/beds/",
                                     hover_image_name = "bed_default_hover", hover_image_path= "images/beds/")

        $ custom_bed_1_OBJ = room_object_class(object_image_name = "custom_bed_1", object_image_path = "images/beds/",
                                     idle_image_name = "custom_bed_1", idle_image_path = "images/beds/",
                                     hover_image_name = "custom_bed_1_hover", hover_image_path= "images/beds/")

        $ default_computer_OBJ = room_object_class(object_image_name = "computer_default", object_image_path = "images/computers/",
                                     idle_image_name = "computer_default", idle_image_path = "images/computers/",
                                     hover_image_name = "computer_default_hover", hover_image_path= "images/computers/")

        $ default_mirror_OBJ = room_object_class(object_image_name = "mirror_default", object_image_path = "images/mirrors/",
                                     idle_image_name = "mirror_default", idle_image_path = "images/mirrors/",
                                     hover_image_name = "mirror_default_hover", hover_image_path= "images/mirrors/")
        return
