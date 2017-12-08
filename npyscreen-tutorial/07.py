#!/usr/bin/env python

import npyscreen


class FormObject(npyscreen.Form):
    def create(self):
        self.show_atx = 30
        self.show_aty = 5
        self.add(npyscreen.TitleText, name='First Name:', begin_entry_at=20)
        self.nextrely += 1
        self.add(npyscreen.TitleText, name='Last Name:')

    def afterEditing(self):
        self.parentApp.setNextForm(None)


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FormObject, name='Npyscreen Test Form', lines=10, columns=40)


if __name__ == "__main__":
    app = App().run()
