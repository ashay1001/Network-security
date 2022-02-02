def isAnagram(str1, str2):
    if(len(str1) != len(str2)):
        return False
    elif set(str1.lower()) == set(str2.lower()):
      return True
    else:
      return False


def main():
    file1 = open('sample.txt', 'r')
    list1 = file1.read().split()
    result = []
    str1 = input("Enter a word to check for anagram: ")
    for i in list1:
        if(isAnagram(i, str1)):
            result.append(i)

    print("Anagram Words from the sample file: ", result)

if __name__ == "__main__":
    main()

    