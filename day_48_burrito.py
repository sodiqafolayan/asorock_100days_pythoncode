# Copy your Burrito class from the last exercise. Now,
# write a getter and a setter method for each attribute.
# Each setter should accept a value as an argument. If the
# value is a valid value, it should set the corresponding
# attribute to the given value. Otherwise, it should set the
# attribute to False.
#
# Edit the constructor to use these new setters and getters.
# In other words, if we were to call:
#
# new_burrito = Burrito("spaghetti", True, True, False)
#
# new_burrito.meat would be False because "spaghetti" is not
# one of the valid options. Note that you should NOT try to
# check if the new value is valid in both the constructor and
# the setter: instead, just call the setter from the
# constructor using something like self.set_meat(meat).
#
# Valid values for each setter are as follows:
#
# - set_meat: "chicken", "pork", "steak", "tofu", False
# - set_to_go: True, False
# - set_rice: "brown", "white", False
# - set_beans: "black", "pinto", False
# - set_extra_meat: True, False
# - set_guacamole: True, False
# - set_cheese: True, False
# - set_pico: True, False
# - set_corn: True, False
#
# Make sure you name each setter with the format:
# "set_some_attribute" and "get_some_attribute"
#
# For example, the getter for meat would be get_meat. The
# getter for to_go would be get_to_go.
#
# Hint: Your code is going to end up *very* long. This
# will be the longest program you've written so far, but
# it isn't the most complex. Complexity and length are
# often very different!
#
# Hint 2: Checking for valid values will be much easier
# if you make a list of valid values for each attribute
# and check the new value against that.


if __name__ == '__main__':
    class Burrito:
        def __init__(self, meat, to_go, rice, beans,
                     extra_meat=False, guacamole=False,
                     cheese=False, pico=False, corn=False):
            self.set_meat(meat)
            self.set_to_go(to_go)
            self.set_rice(rice)
            self.set_beans(beans)
            self.set_extra_meat(extra_meat)
            self.set_guacamole(guacamole)
            self.set_cheese(cheese)
            self.set_pico(pico)
            self.set_corn(corn)

        # GETTERS
        def get_meat(self):
            return self.meat

        def get_to_go(self):
            return self.to_go

        def get_rice(self):
            return self.rice

        def get_beans(self):
            return self.beans

        def get_extra_meat(self):
            return self.extra_meat

        def get_guacamole(self):
            return self.guacamole

        def get_cheese(self):
            return self.cheese

        def get_pico(self):
            return self.pico

        def get_corn(self):
            return self.corn

        # SETTERS
        def set_meat(self, new_meat):
            if new_meat in {"chicken", "pork", "steak", "tofu", False}:
                self.meat = new_meat
            else:
                self.meat = False

        def set_to_go(self, new_to_go):
            if new_to_go in {True, False}:
                self.to_go = new_to_go
            else:
                self.to_go = False

        def set_rice(self, new_rice):
            if new_rice in {"brown", "white", False}:
                self.rice = new_rice
            else:
                self.rice = False

        def set_beans(self, new_beans):
            if new_beans in {"black", "pinto", False}:
                self.beans = new_beans
            else:
                self.beans = False

        def set_extra_meat(self, new_extra_meat):
            if new_extra_meat in {True, False}:
                self.extra_meat = new_extra_meat
            else:
                self.extra_meat = False

        def set_guacamole(self, new_guacamole):
            if new_guacamole in {True, False}:
                self.guacamole = new_guacamole
            else:
                self.guacamole = False

        def set_cheese(self, new_cheese):
            if new_cheese in {True, False}:
                self.cheese = new_cheese
            else:
                self.cheese = False

        def set_pico(self, new_pico):
            if new_pico in {True, False}:
                self.pico = new_pico
            else:
                self.pico = False

        def set_corn(self, new_corn):
            if new_corn in {True, False}:
                self.corn = new_corn
            else:
                self.corn = False


    # The code below will test your class. If it is written
    # correctly, this will print True, then False. Note,
    # though, that we'll test your code against more complex
    # test cases when you submit.
    newBurrito = Burrito("Tofu", True, True, True)
    print(newBurrito.to_go)
    print(newBurrito.guacamole)