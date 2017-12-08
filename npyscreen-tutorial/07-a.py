#!/usr/bin/env python

import npyscreen


class FormObject(npyscreen.ActionFormV2):
    def create(self):
        self.show_atx = 30
        self.show_aty = 5
        self.fname = self.add(npyscreen.TitleText, name='First Name:')
        self.nextrely += 1
        self.lname = self.add(npyscreen.TitleText, name='Last Name:')

    def afterEditing(self):
        # self.parentApp.setNextForm(None)
        pass

    def on_ok(self):
        # pass
        self.fname.value = "Ok button pressed!"

    def on_cancel(self):
        # pass
        self.lname.value = "Cancel button pressed!"


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FormObject, name='Npyscreen Test Form', lines=10, columns=60)


if __name__ == "__main__":
    app = App().run()
    # print(FormObject().fname)
