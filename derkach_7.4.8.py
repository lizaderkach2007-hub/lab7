import copy
import os


class SentenceError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Sentence:
    def __init__(self, sentence=None):
        if sentence is None:
            self.words = []
        elif isinstance(sentence, Sentence):
            self.words = copy.deepcopy(sentence.words)
        elif isinstance(sentence, list):
            self.words = [str(word) for word in sentence]
        elif isinstance(sentence, str):
            self.words = sentence.split()
        else:
            raise SentenceError("Initial value must be a string, list or Sentence instance.")

    def __len__(self) -> int:
        return len(self.words)

    def __getitem__(self, index: int) -> str:
        return self.words[index]

    def __setitem__(self, index: int, value: str):
        if not isinstance(value, str):
            raise SentenceError("New value must be a string.")
        self.words[index] = value

    def __contains__(self, word: str) -> bool:
        return str(word) in self.words

    def __add__(self, other):
        if isinstance(other, Sentence):
            return Sentence(self.words + other.words)
        elif isinstance(other, str):
            return Sentence(self.words + [other])
        else:
            raise SentenceError("Addition failed: Right operand must be an instance of Sentence or a string.")

    def __sub__(self, other):
        if isinstance(other, Sentence):
            other_words = other.words
            return Sentence([word for word in self.words if word not in other_words])
        elif isinstance(other, str):
            return Sentence([word for word in self.words if word != other])
        else:
            raise SentenceError("Subtraction failed: Right operand must be an instance of Sentence or a string.")

    def __str__(self) -> str:
        return " ".join(self.words)

    def __repr__(self) -> str:
        return f"Sentence('{self.__str__()}')"


def main():
    input_file = "input.txt"
    output_file = "output.txt"

    if not os.path.exists(input_file):
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write("Це тестове речення для перевірки лабораторної роботи з ООП")

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()

        if not content:
            print("Вхідний файл порожній.")
            return

        sentence = Sentence(content)
        
        log_lines = []
        log_lines.append(f"Початковий текст: {sentence}")
        log_lines.append(f"Загальна кількість слів: {len(sentence)}")

        if len(sentence) > 2:
            sentence[2] = "модифіковане"
            log_lines.append(f"Після заміни третього слова: {sentence}")

        sentence = sentence - "тестове"
        log_lines.append(f"Після видалення слова 'тестове': {sentence}")

        sentence = sentence + "завершено"
        log_lines.append(f"Після додавання слова 'завершено': {sentence}")
        log_lines.append(f"Кінцева кількість слів: {len(sentence)}")

        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.write("\n".join(log_lines) + "\n")

        print("Програма успішно виконала всі прикладні завдання 5.4.8.")
        print(f"Результати обробки та кроки записано у файл '{output_file}'.")

    except SentenceError as e:
        print(f"Помилка бізнес-логіки класу Sentence: {e.message}")
    except (IOError, OSError) as e:
        print(f"Помилка під час роботи з файлами: {e}")


if __name__ == "__main__":
    main()
