#!/usr/bin/env python

import npyscreen


class FormObject(npyscreen.Form):
    def create(self):
        test_list=['1', '2', '3']
        self.add(npyscreen.TitleText, name='First Name:', begin_entry_at=20)
        self.add(npyscreen.TitleText, name='Last Name:')

    def afterEditing(self):
        self.parentApp.setNextForm(None)


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FormObject, name='Npyscreen Test Form')


if __name__ == "__main__":
    app = App().run()
