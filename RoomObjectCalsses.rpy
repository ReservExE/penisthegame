init -1 python:
    class room_object_class:
        def __init__(self,
                    object_image_name, object_image_path,
                    idle_image_name, idle_image_path,
                    hover_image_name, hover_image_path):

            self.object_image_name = object_image_name
            self.object_image_path = object_image_path

            self.idle_image_name = idle_image_name
            self.idle_image_path = idle_image_path

            self.hover_image_name = hover_image_name
            self.hover_image_path = hover_image_path

        def get_object_image(self):
            if self.object_image_path != "":
                return "" +str(self.object_image_path)+ "" +str(self.object_image_name)+ ".png"
            else:
                return self.object_image_name

        def get_idle_image(self):
            if self.idle_image_path != "":
                return "" +str(self.idle_image_path)+ "" +str(self.idle_image_name)+ ".png"
            else:
                return self.idle_image_name

        def get_hover_image(self):
            if self.hover_image_path != "":
                return "" +str(self.hover_image_path)+ "" +str(self.hover_image_name)+ ".png"
            else:
                return self.hover_image_name
