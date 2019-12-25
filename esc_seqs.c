// Program: esc_seqs.c (escape sequences)
// Author: Trevor Martin
// Date of Completion: 7 July 2019
// Language: C

//=======================================================================================================
// INFORMATION ------------------------------------------------------------------------------------------
//=======================================================================================================

// Compile: clang esc_seqs.c -o esc_seqs
// Run: ./esc_seqs

//=======================================================================================================

// [1] What are the escape sequences in C and how do you use them? 

# include <stdio.h>

// there are different escape sequences in C

int main(void)
{
  // \r is carriage return, it only returns everything after it
  // \n new line
  // \a alarm or beep
  // \t horizontal tab
  // \v vertical tab
  // \ooo  octal number
  // \xhh  hexadecimal number
  // \" double quote
  // \' single quote
  // \? question mark
  // \\ backslash

  // line splicing \ <-- this backslash makes the next printf statement a comment too
  printf("Line splicing is is when you use a \\ to conjoin (splice) a line with the line before it!\n");
  printf("If you do not practice them you will forget them.\n");
  return (0);
}

//=======================================================================================================
// End of Program ---------------------------------------------------------------------------------------
//=======================================================================================================
