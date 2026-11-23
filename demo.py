try:
  a = 10
  b = "10"
  print(a/b)
except ZeroDivisionError:
  print("zero divison error")
except TypeError:
  print("Data type is invalid")
except Exception as e:
  print(e)