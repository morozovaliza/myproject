def preprocess_text(text, low=True, filter_puncts=True, lemmatize=True):
    import nltk
    nltk.download('punkt', quiet=True)

    if low:
        text = text.lower()
    # Проводим токенизацию текста по словам

    en_tokens = nltk.word_tokenize(text)

    # Фильтрация по стоп-словам
    from nltk.corpus import stopwords

    nltk.download('stopwords', quiet=True)
    stopwords = stopwords.words('english')
    filtered_tokens = [i for i in en_tokens if i not in stopwords]
    print ("Проводим токенизацию текста по словам:")
    print (" ".join(filtered_tokens))

    # Фильтрация знаков пунктуации
    if filter_puncts:
        marks = '/.,!&^%$-;:'
        filtered_tokens = [i for i in filtered_tokens if i not in marks]
    print ("Фильтрация знаков пунктуации:")
    print (" ".join(filtered_tokens))

    # Лемматизация
    if lemmatize:
        nltk.download('wordnet', quiet=True)
        nltk.download('omw-1.4', quiet=True)
        wordnet_lemmatizer = nltk.WordNetLemmatizer()
        result = []
        for word in filtered_tokens:
            result.append(wordnet_lemmatizer.lemmatize(word))
        print ("Лемматизация:")
        print (" ".join(result))
        return result

    # Стемминг
    else:
        p_stemmer = nltk.PorterStemmer()
        result = []
        for word in filtered_tokens:
            result.append(p_stemmer.stem(word))
        print ("Стемминг:")
        print (" ".join(result))
        return result


text = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms."

text_2 = "This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well."

print("Вывод:\n" + " ".join(preprocess_text(text)) + "\n")
print("Вывод:\n" + " ".join(preprocess_text(text_2, lemmatize=False)) + "\n")
