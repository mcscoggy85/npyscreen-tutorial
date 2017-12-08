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
        npyscreen.notify_confirm("Ok button was pressed", "Saved!!", editw=1)
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        exiting = npyscreen.notify_yes_no("Are you sure you want to cancel", "Positive?", editw=2)
        if exiting:
            npyscreen.notify_confirm("Form has not been saved", 'bye bye', editw=1)
            self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("You can continue working", 'okay', editw=1)


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FormObject, name='Npyscreen Test Form', lines=10, columns=60)


if __name__ == "__main__":
    app = App().run()
    # print(FormObject().fname)
