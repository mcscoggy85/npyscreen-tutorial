#!/usr/bin/env python

import npyscreen


def simple_function(*args):
        form = npyscreen.Form(name='Npyscreen Form!')
        form.edit()


if __name__ == "__main__":
    npyscreen.wrapper_basic(simple_function)
    print("This is a test app")
