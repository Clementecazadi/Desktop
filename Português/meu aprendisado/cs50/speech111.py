from google_speech import Speech
response = Speech("You say ", 'en')
response.play()
son_effets = ("speech", "1.5")
response.play(son_effets)