import re
def main():
    print("--- Begin report of books/frankenstein.txt ---")
    book = get_book_text('books/frankenstein.txt')
    count = wordCount(book)
    print(f"{count} words found in the document")
    dict = count_duplicates(book)
    for key,value in dict.items():
      print(f"The {key} character was found {value} times")

def wordCount(input):
  # error is that im counting all of the spaces
  input = input.split()
  return len(input)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_duplicates(string):
  before = string.lower()
  lower = re.sub(r'[^a-zA-Z]', '', before)
  dict = {}
  for c in lower:
    if c not in dict:
      dict[c] = 1
    else:
      dict[c] += 1
  return dict



if __name__ == '__main__':
  main()