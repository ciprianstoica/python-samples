class Palindrome:
  @staticmethod
  def is_palindrome(word):
    lc_word = word.lower()
    len_word = len(word)
    half_len = len_word // 2
    for i in range(0, half_len):
      if lc_word[i] != lc_word[len_word - i - 1]:
        return False
    return True
word = input()
print(Palindrome.is_palindrome(word))