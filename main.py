from general import VoiceService
import phrases
from actions import Actions


class MainLogic(VoiceService):
    def __init__(self):
        super().__init__()
        self.action = Actions()

    def main_logic(self):
        """
            Основная логика опроса
            :return:
        """
        phrase = phrases.MAIN_LOGIC
        self.nn.counter('main_count')
        entities = [
            'recommendation_score', 'recommendation', 'repeat', 'wrong_time',
            'question',
        ]
        phrase_tuple = (
            phrase.get('recommend_main'), phrase.get('recommend_null'))
        self.nn.counter('recommend_main_count')
        recognition_result = self.loop_synth_and_recognize(
            'recommend_main_count', 2,
            phrase_tuple,
            entities=entities)
        if not recognition_result:
            self.action.hangup_null()

        if recognition_result.has_entity('repeat'):
            self.nn.counter('recommend_repeat_count')
            phrase_tuple = (
                phrase.get('recommend_repeat'),
                phrase.get('recommend_default'))
            recognition_result = self.loop_synth_and_recognize(
                'recommend_main_count', 2,
                phrase_tuple,
                entities=entities)
            if not recognition_result:
                self.action.hangup_null()
        self.parse_recommendation_score(recognition_result)
        if recognition_result.has_entity('wrong_time'):
            self.action.hangup_wrong_time()
        if recognition_result.entity('recommendation') == 'negative':
            text = phrase.get('recommend_score_negative')
            recognition_result = self.synth_and_recognize(text,
                                                          entities=entities)
            if not recognition_result:
                self.action.hangup_null()
            self.parse_recommendation_score(recognition_result)
        if recognition_result.entity('recommendation') == 'positive':
            text = phrase.get('recommend_score_positive')
            recognition_result = self.synth_and_recognize(text,
                                                          entities=entities)
            if not recognition_result:
                self.action.hangup_null()
            self.parse_recommendation_score(recognition_result)
        if recognition_result.entity('recommendation') == 'dont_know':
            text = phrase.get('recommend_repeat_2')
            recognition_result = self.synth_and_recognize(text,
                                                          entities=entities)
            if not recognition_result:
                self.action.hangup_null()
            self.parse_recommendation_score(recognition_result)
        if recognition_result.entity('question') == 'true':
            self.action.forward()
        self.action.hangup_null()

    def parse_recommendation_score(self, recognition_result):
        """
        Парсит значения сущности recommendation_score
        :param recognition_result: результат распознования
        :return:
        """
        if recognition_result.has_entity('recommendation_score'):
            if recognition_result.entity('recommendation_score') in range(0,
                                                                          9):
                self.action.hangup_negative()
            elif recognition_result.entity('recommendation_score') in range(9,
                                                                            11):
                self.action.hangup_positive()
