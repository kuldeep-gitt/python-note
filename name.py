def func():
    print("func() is called")

print("Top level of name.py")

if __name__ == '__main__':
    print("name.py run directly")
else:
    print("name.py not run directly")
