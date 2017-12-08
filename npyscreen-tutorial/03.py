#!/usr/bin/env python

import npyscreen


class FormObject(npyscreen.Form):
    def create(self):
        pass

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FormObject, name='Npyscreen Form!')


if __name__ == "__main__":
    app = App().run()
    print("This is a test app")
