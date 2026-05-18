class SentenceError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Sentence:
    def __init__(self, sentence):
        if not isinstance(sentence, str):
            raise SentenceError("Initial sentence must be a string.")
        self.words = sentence.split()

    def __len__(self):
        return len(self.words)

    def __getitem__(self, index):
        return self.words[index]

    def __setitem__(self, index, value):
        if not isinstance(value, str):
            raise SentenceError("New value must be a string.")
        self.words[index] = value

    def __contains__(self, word):
        return word in self.words

    def __add__(self, other):
        if isinstance(other, Sentence):
            return Sentence(" ".join(self.words + other.words))
        elif isinstance(other, str):
            return Sentence(" ".join(self.words + [other]))
        else:
            raise SentenceError("Right operand must be an instance of Sentence or a string.")

    def __sub__(self, other):
        if isinstance(other, Sentence):
            return Sentence(" ".join([word for word in self.words if word not in other.words]))
        elif isinstance(other, str):
            return Sentence(" ".join([word for word in self.words if word != other]))
        else:
            raise SentenceError("Right operand must be an instance of Sentence or a string.")

    def __repr__(self):
        return " ".join(self.words)

try:
    s1 = Sentence("Це просте речення для тестування")
    s2 = Sentence("Це ще одне речення")
    print(s1)  
    print(len(s1))  
    print(s1[2])  
    s1[2] = "слово"
    print(s1)  

    s3 = s1 + s2
    print(s3)  
    s4 = s1 + "додаткове"
    print(s4)
    
    s5 = s1 - "слово"
    print(s5)  
    s6 = s1 - s2
    print(s6)  

    print("слово" in s1)  
    print("не існуюче" in s1)  

    s1[2] = 123  
except SentenceError as e:
    print(e.message)

try:
    s_invalid = Sentence(123)  
except SentenceError as e:
    print(e.message)
