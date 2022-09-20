k = input("Masukkan Kata: ")
def is_palindrome(w):
  rw = str(w)[::-1]
  if str(w) == rw:
    return True
  return False

print(is_palindrome(k))