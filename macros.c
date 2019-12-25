// Program: macros.c
// Author: Trevor Martin
// Date of Completion: 7 July 2019
// Language: C

//=======================================================================================================
// INFORMATION ------------------------------------------------------------------------------------------
//=======================================================================================================

// Compile: clang macros.c -o macros
// Run: ./macros

//=======================================================================================================

// [1] What are macros in C?
// [2] What can you do with macros in C?
// [3] How does undefining macros work in C?

# include <stdio.h>
# define wicked 696969
// # define wicked = 696969 <-- doesn't work
# define function1(input) input*input // <-- evaluates 2+3 as 2 + 3*3 + 2
# define function2(input) (input)*(input) // <-- evaluates 2+2 as (2+3)*(2+3)
# define function3(input,limiter) while (input < limiter)\
                                  {\
				    printf("%s %d %s\n","T minus",limiter-input,"seconds.");\
				    input++;\
				  }
# define concat(input1,input2) input1##input2 // <-- (69,69) comes out as 6969, concats tokens
# define make_string(input) #input // <-- token converted to string literal
 
int main()
{
  
  // printf("Five 5"); --> Five 5
  // printf("%s %d","Five",5); --> Five 5
  // printf("Five %d",5); --> Five 5
  
  printf("quote percent s quote, __FILE___: %s\n",__FILE__);
  printf("quote percent s quote, __TIME___: %s\n",__TIME__);
  printf("quote percent s quote, __DATE___: %s\n",__DATE__);
  printf("quote percent d quote, __LINE___: %d\n",__LINE__);

  int a = function1(6 + 3);
  int b = function2(6 + 3);
  printf("%s %d, %s %d\n","Int a:",a,"Int b:",b);
  
  int input = 1;
  function3(input,10);

  printf("%s\n",make_string(Fuck_off_Lehey));
  
  printf("%s %d\n","concat(69,69):",concat(69,69));

  // --> # undef wicked concat make_string
  // produces...
  // macros.c:51:18: warning: extra tokens at end of #undef directive [-Wextra-tokens]
  // # undef wicked concat make_string
  //               ^
  // 1 warning generated.

  // each undef must have its own line
  # undef wicked
  # undef concat 
  # undef make_string
  # undef function1
  # undef function2 
  # undef function3

  int wicked = 11111;
  char concat = 'y';
  char make_string[100] = "Trevor is a human bean.";
  printf("%d %c %s\n",wicked,concat,make_string);

  return (0);
}

//=======================================================================================================
// End of Program ---------------------------------------------------------------------------------------
//=======================================================================================================
