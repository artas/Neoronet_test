from general import VoiceService
import phrases


class Actions(VoiceService):
    def __init__(self):
        super(Actions, self).__init__()

    def hangup_wrong_time(self):
        phrase = phrases.HANGUP_LOGIC
        self.nn.log('tag', 'нет времени для разговора')
        text = phrase.get('hangup_wrong_time')
        self.nv.synthesize(text)
        self.nn.dialog.result = self.nn.wrong_time

    def hangup_null(self):
        phrase = phrases.HANGUP_LOGIC
        self.nn.log('tag', 'проблемы с распознаванием')
        text = phrase.get('hangup_null')
        self.nv.synthesize(text)
        self.nn.dialog.result = self.nn.null

    def hangup_negative(self):
        phrase = phrases.HANGUP_LOGIC
        self.nn.log('tag', 'низкая оценка')
        text = phrase.get('hangup_negative')
        self.nv.synthesize(text)
        self.nn.dialog.result = self.nn.negative

    def hangup_positive(self):
        phrase = phrases.HANGUP_LOGIC
        self.nn.log('tag', 'высокая оценка')
        text = phrase.get('hangup_positive')
        self.nv.synthesize(text)
        self.nn.dialog.result = self.nn.positive

    def forward(self):
        phrase = phrases.FORWARD_LOGIC
        self.nn.log('tag', 'перевод на оператора')
        text = phrase.get('forward')
        self.nv.synthesize(text)
        self.nv.bridge('xxx-xxx-xxx')
