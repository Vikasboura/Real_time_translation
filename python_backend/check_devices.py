import speech_recognition as sr

print("--- Listing Available Audio Input Devices ---")
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Index {index}: {name}")
