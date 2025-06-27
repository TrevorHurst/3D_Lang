# 3D_Lang
Three Dimensional Esoteric Programming Language


Extremely similar to the Befunge languge but, 3 dimensional, adding instructions for 3 dimensional movement.

The z-planes may be added by creating files "planeX.3D"

Happy coding!

## Command Set

> - left
< - right
^ - up
v - down
} - next plane
{ - previous plane
+ - add next val to top num
# - delete top of the stack
- - subtract from top stack
* - multiply next val to top num
/ - top/next
$ - Jump over next spot
@ - double jump
? - compare top two in stack left/right
! - compare top two in stack fd/back
| - compare top two in stack up/down
/ - swap top two values
p - put to spot [x,y,z]
g - read from spot [x,y,z]
. - print num
, - print ascii char
' - start/stop reading string
& - end code
) - user input number to top of stack
( - user input character to top of stack