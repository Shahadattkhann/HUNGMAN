def design(lives):
      if lives ==5:

          print("______\n"
                "      |\n"
                "      |\n"
                "      |\n"
                "      |\n"
                "      |")
      elif lives==4:
            print("______\n"
                  "  |   |\n"
                  "      |\n"
                  "      |\n"
                  "      |\n"
                  "      |")
      elif lives==3:
            print("______\n"
                  "  |   |\n"
                  " ( )  |\n"
                  "      |\n"
                  "      |\n"
                  "      |")
      elif lives ==2:
            print("______\n"
                  "  |   |\n"
                  " ( )  |\n"
                  " /|\  |\n"
                  "      |\n"
                  "      |")
      elif lives == 1:
            print("______\n"
                  "  |   |\n"
                  " ( )  |\n"
                  " /|\  |\n"
                  "  |   |\n"
                  "      |")
      elif lives == 0:
            print("______\n"
                  "  |   |\n"
                  " ( )  |\n"
                  " /|\  |\n"
                  "  |   |\n"
                  " / \  |")
if __name__ == '__main__':
      for i in range(0,6):
            design(i)
