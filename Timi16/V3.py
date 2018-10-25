# class Sentence():
#     def __init__(self, sentence):
#         self.sentence = sentence
#         self.list_of_words = sentence.split()
    
#     def get_first_word(self):
#         return self.list_of_words[0]
    
#     def get_all_words(self):
#         return self.list_of_words
    
#     def replace(self, index, new_word):
#         try:
#             self.list_of_words[index] = new_word
#             return self.list_of_words
#         except:
#             pass

def main():
    sent = Sentence('This is a test')
    print(sent.get_first_word())
    assert str(sent.get_first_word()) == "This"

    print(sent.get_all_words())
    assert sent.get_all_words() == 'This is a test'.split()

    sent.replace(3, "must")
    print(sent.get_all_words())
    assert sent.get_all_words() == 'This is a must'.split()
  
main()
