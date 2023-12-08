word = input("Слово для пошуку: ")
file_path = "/Users/smurslik/Downloads/In the heart of a bustling city.txt"
word_found = False
with open(file_path, 'r') as file:
    paragraphs = file.read().split('\n\n')
    for i, paragraph in enumerate(paragraphs, 0):
        words = paragraph.lower().split()
        if word.lower() in words:
            print(f"{paragraph}")
            word_found = True
        if not word_found:
            print("немає такого слова")
