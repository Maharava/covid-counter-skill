from mycroft import MycroftSkill, intent_file_handler


class CovidCounter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('counter.covid.intent')
    def handle_counter_covid(self, message):
        self.speak_dialog('counter.covid')


def create_skill():
    return CovidCounter()

