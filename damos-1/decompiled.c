int main(int argc,char **argv)
{
  size_t serial_length;
  int counter;
  bool serial_is_correct;
  counter = 0;

  if (argc < 2) {
    printf("Usage: %s <serial>\n",*argv);
  }
  else {
    serial_length = strlen(argv[1]);
    if (serial_length == 10) {
      while (argv[1][counter] != '\0') {
        if (('`' < argv[1][counter]) && (argv[1][counter] < '{')) {
          argv[1][counter] = argv[1][counter] + -0x20;
        }
        counter = counter + 1;
      }
      if ((int)*argv[1] == (int)argv[1][9] + -3) {
        if ((int)argv[1][1] == (int)argv[1][8] + 0xe) {
          if ((int)argv[1][2] == (int)argv[1][7] + -0x14) {
            if ((int)argv[1][3] == (int)argv[1][6] + 6) {
              if (((int)argv[1][4] + (int)argv[1][5]) / 2 == (int)*argv[1]) {
                serial_is_correct = true;
              }
              else {
                serial_is_correct = false;
              }
            }
            else {
              serial_is_correct = false;
            }
          }
          else {
            serial_is_correct = false;
          }
        }
        else {
          serial_is_correct = false;
        }
      }
      else {
        serial_is_correct = false;
      }
      if (serial_is_correct) {
        printf("%s\n","Good Serial!");
      }
      else {
        printf("%s\n","Bad Serial!");
      }
    }
    else {
      printf("%s\n","Bad Serial!");
    }
  }
  return 0;
}