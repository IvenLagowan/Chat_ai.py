print("🤖 Asisten AI Sederhana")
print("Ketik 'exit' untuk keluar\n")

while True:
    user = input("Kamu: ").lower()

    if user == "exit":
        print("AI: Sampai jumpa! 👋")
        break

    elif "halo" in user:
        print("AI: Halo juga! 😊")

    elif "apa kabar" in user:
        print("AI: Saya baik, kamu gimana?")

    elif "siapa kamu" in user:
        print("AI: Saya asisten AI sederhana buatan kamu 😎")

    elif "jam" in user:
        import datetime
        now = datetime.datetime.now()
        print("AI: Sekarang jam", now.strftime("%H:%M"))

    elif "terima kasih" in user:
        print("AI: Sama-sama! 🙏")

    elif "belajar" in user:
        print("AI: Semangat belajar! Coding itu skill masa depan 🚀")

    else:
        print("AI: Maaf, saya belum mengerti 😅")
