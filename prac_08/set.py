from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
# import random
from kivy.properties import StringProperty

class HelloWorld(App):
    message = StringProperty()

    def build(self):
        self.title = 'Hello World'
        self.root = Builder.load_file("box_layout.kv")
        return self.root

    def handle_press(self):
        self.message = self.root.ids.user_input.text




    # def press_button(self):
    #     if random.randont(1,20) <=10:
    #         self.root.ids.my_label.text = "ouch!"
    #     else:
    #         self.root.ids.my_label.text = "hello"



    # def press_button(self,button):
    #     print(f"{button.text} says ouch!")


    # def release_button(self):
    #     print("hello")

# class TestApp(App):
#     def build(self):
#         return Button(text="Hello, test")




HelloWorld().run()
TestApp().run()
