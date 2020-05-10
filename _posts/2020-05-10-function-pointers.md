### Function Pointers in C

How do you decipher a statement like this?

```C
int (*pf)(int, int)
```

This is a function pointer in C and can be read: "declare pf as pointer to function (int, int) returning int".

It fits into a larger program as such:

```C
#include <stdio.h>

int addAtoB(int a, int b) {
        return a + b;
}

int main() {
        int (*pf)(int, int);
        pf = &addAtoB;
        int x = pf(2,3);

        printf("x: %d", x);
        
        return 0;
}
```
A function called addAtoB is created that takes two parameters and returns their sum. Within main a pointer to a function is created and named pf. The address of the function addAtoB is then assigned to the pointer pf. A variable called x is created and the values 2 and 3 are passed to the pointer.

This behavior can be also be replicated using typdef. 

```C
typedef int (*pf)(int, int);
...

pf p = &addAtoB;
int x2 = (*p)(2,3);
printf("x2: %d", x2);
```


Notes:
A great website for translating these statements is: https://cdecl.org/
