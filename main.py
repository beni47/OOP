
import json
import difflib #suggests words incase of a typo
file_path = r"C:\Users\LENOVO\Desktop\PYTHON\OOP\OOP\dictionary-data-master\data.json"

with open(file_path) as f:
      dict_data = json.load(f)


def get_definition(word,dict_data):
      word = word.lower()
      definition = dict_data.get(word)

    #performs a case-insensitive search for the input word
      if definition is None:
        for key in dict_data.keys():
            if key.lower() == word:
                definition = dict_data[key]
                break

    # If the word is still not found, suggest a similar word
      if definition is None:
        similar_words = difflib.get_close_matches(word, dict_data.keys(), n=1)
        if similar_words:
            suggestion = similar_words[0]
            response = input(f"Did you mean '{suggestion}' instead? Enter Y if yes, or N if no: ").lower()
            if response == 'y':
                definition = dict_data[suggestion]

      return definition if definition is not None else "Definition not found."


word = input("Enter a word to get its definition: ")
definition = get_definition(word, dict_data)
print(definition)