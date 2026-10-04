print("Welcome! I am a basic chatbot.Type something to start chatting.")
while True:
    you=input("you:").lower()
    if(you=="hi" or you=="hello"):
        print("👋 Hi! How can I help you?")
    elif(you=="how are you"):
        print("😊 I'm fine, thanks! How are you?")
    elif(you=="fine"or you=="good"):
        print("Glad to hear that! ✨☺️")
    elif(you=="what is your name"):
        print("I'm a basic python chatbot.")
    elif(you=="what can you do"):
        print("💬 I can have a simple conversation with you.")
    elif(you=="help"):
        print("I can respond to greetings, simple questions, and goodbye.")
    elif(you=="thank you" or you=="thanks"):
        print("You're welcome! 😊")
    elif(you=="bye"):
        print("👋 Goodbye! Take care!")
        break
    elif(you=="good morning"):
        print("Good Morning! Have a Great Day!")
    elif(you=="what is python"):
        print("python is a popular programming language.")
    else:
        print(" Sorry, I don't understand that.")
    