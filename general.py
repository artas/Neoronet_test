from NeurNet import (
    NeuroNluLibrary,
    NeuroVoiceLibrary,
    NeuroNetLibrary
)


class VoiceService:
    nlu_call = None
    event_loop = None

    def __init__(self):
        self.nlu = NeuroNluLibrary(self.nlu_call, self.event_loop)
        self.nv = NeuroVoiceLibrary(self.nlu_call, self.event_loop)
        self.nn = NeuroNetLibrary(self.nlu_call, self.event_loop)

    def synth_and_recognize(
            self, text: str, ssml: bool = False,
            detect_policy: [tuple, str, int, None] = None,
            entities: [list, str, None] = None,
            entities_exclude: str = None,
            intents: [list, str, None] = None,
            intents_exclude: str = None,
            context: str = None,
            use_neuro_api: bool = False
            ) -> object:
        """
        Запускает синтез и распознование
        :return: результат разпознования
        """
        self.nv.synthesize(text, ssml)
        with self.nv.listen(detect_policy,
                            entities,
                            entities_exclude,
                            intents,
                            intents_exclude,
                            context,
                            use_neuro_api
                            ) as recognition_result:
            return recognition_result

    def loop_synth_and_recognize(
            self, counter_name: str, attempts: int,
            phrases: tuple, called_name: str = None,
            *args, **kwargs
            ):
        """

        :param counter_name: имя счетчика
        :param attempts: количество попыток распознавания
        :param phrases: картедж с фразами
        :param called_name: Имя вызываемого(опционально)
        :param args:
        :param kwargs:
        :return: результат распознавания если успешно, иначе None
        """
        while self.nn.counter(counter_name) < attempts:
            if called_name and self.nn.counter(counter_name) == 0:
                text = f'{called_name}{phrases[self.nn.counter(counter_name)]}'
            else:
                text = phrases[attempts]
            recognition_result = self.synth_and_recognize(text, *args,
                                                           **kwargs)
            if not recognition_result.has_entities():
                self.nn.counter(counter_name, '+')
                continue
            else:
                return recognition_result

