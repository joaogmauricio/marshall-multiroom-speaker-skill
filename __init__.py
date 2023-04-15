from mycroft import MycroftSkill, intent_file_handler


class MarshallMultiroomSpeaker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('speaker.multiroom.marshall.intent')
    def handle_speaker_multiroom_marshall(self, message):
        preset = message.data.get('preset')

        self.speak_dialog('speaker.multiroom.marshall', data={
            'preset': preset
        })


def create_skill():
    return MarshallMultiroomSpeaker()

