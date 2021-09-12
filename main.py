from gtts import gTTS
tts = gTTS('我不明白你的問題，請再重複一次', lang='zh')
tts.save('hello.mp3')
tts2=gTTS('好的，現在時間是2月2號，請繫上安全帶，我們即將前往8D時空。', lang='zh')
tts2.save('好的現在時間是2月2號請繫上安全帶我們即將前往8D時空.mp3')
