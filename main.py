import threading

from TTS.api import TTS

# Running a multi-speaker and multi-lingual model

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
tts = TTS(model_name)


# Run TTS
# ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
def test_TTS(count=0, example_text=''):
    print(count)

    wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
    # Text to speech to a file
    tts.tts_to_file(text=example_text, speaker=tts.speakers[0], language=tts.languages[0],
                    file_path="output" + str(count) + ".wav")


if __name__ == '__main__':
    params = {"count": 1,
              "example_text": 'the birch canoe slid on the smooth planks grew the sheet to the dark blue background '
                              'it\'s easy to tell the depth of a well four hours of steady work faced us'}
    task_listen = threading.Thread(name="test_speak", target=test_TTS, kwargs=params)
    task_listen.start()
