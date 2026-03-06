import sys
input = sys.stdin.readline

n = int(input())
word_dict = {}

def shortcut_key_capital(word_list) :
  for i in range(len(word_list)) :
    cap_word = word_list[i][0].capitalize()
    if word_dict.get(cap_word, 0) == 0 :
        word_dict[cap_word] = 1
        return True, i
  return False, 0

def shortcut_key_all(word_list) :
  for i in range(len(word_list)) :
    for j in range(1, len(word_list[i])) :
      cap_word = word_list[i][j].capitalize()
      if word_dict.get(cap_word, 0) == 0 :
        word_dict[cap_word] = 1
        return True, i, j
  return False, 0, 0

def change_word(word, idx) :
  return word[:idx] + '[' + word[idx] + ']' + word[idx+1:]

answer = []
for _ in range(n) :
  word_list = list(input().rstrip().split(' '))

  is_shortcut_key_capital, idx = shortcut_key_capital(word_list)

  if is_shortcut_key_capital :
    word_list[idx] = change_word(word_list[idx], 0)
  else :
    is_shortcut_key, i, j = shortcut_key_all(word_list)
    if is_shortcut_key :
      word_list[i] = change_word(word_list[i], j)

  answer.append(word_list)

for a in answer :
  print((' ').join(a))