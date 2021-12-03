from general import VoiceService
import phrases
from actions import Actions
from main import MainLogic


class HelloLogic(VoiceService):
    def __init__(self):
        super().__init__()
        self.action = Actions()

    def run(self) -> None:
        """
        Логика приветствия
        :return: None
        """

        # Подразумевается, что в пользовательском хранилище уже есть Name
        phrase = phrases.HELLO_LOGIC
        name = self.nn.storage('Name')
        entities = ['confirm', 'wrong_time', 'repeat']
        self.nn.counter('hello_count')
        phrase_tuple = (phrase.get('hello'), phrase.get('hello_null'))
        recognition_result = self.loop_synth_and_recognize('hello_count', 2,
                                                           phrase_tuple,
                                                           name,
                                                           entities=entities)

        if not recognition_result:
            self.action.hangup_null()

        if recognition_result.has_entity('repeat'):
            text = phrase.get('hello_repeat')
            recognition_result = self.synth_and_recognize(text,
                                                          entities=entities)
            if not recognition_result.has_entities():
                self.action.hangup_null()

        elif recognition_result.has_entity('confirm'):
            if recognition_result.entity('confirm'):
                main_logic = MainLogic()
                main_logic.main_logic()
            else:
                self.action.hangup_wrong_time()
        elif recognition_result.has_entity('wrong_time'):
            self.action.hangup_wrong_time()
        self.action.hangup_null()
