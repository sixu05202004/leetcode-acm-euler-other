#!/usr/bin/env python
# -*- coding: utf-8 -*-
out = []


def proc(n):
    result = "Impossible."
    if n[0] == -1:
        if n[2] >= n[1] and n[1] >= 0:
            s = (n[2] ** 2 - n[1] ** 2) ** 0.5
            result = "a = %.3f" % s
    elif n[1] == -1:
        if n[2] >= n[0] and n[0] >= 0:
            s = (n[2] ** 2 - n[0] ** 2) ** 0.5
            result = "b = %.3f" % s
    elif n[2] == -1:
        if n[0] >= 0 and n[1] >= 0:
            s = (n[1] ** 2 + n[0] ** 2) ** 0.5
            result = "c = %.3f" % s
    return result


def zoj_1241():

    while True:

        line = raw_input()
        if "0 0 0" in line:
            break
        else:
            line = line.split()
            line = [int(i) for i in line]
            t = proc(line)
            out.append(t)

    for i in range(len(out) - 1):
        print "Triangle #%d" % (i + 1)
        print out[i]
        print ""
    print "Triangle #%d" % len(out)
    print out[-1]


if __name__ == '__main__':
    zoj_1241()


#include <stdio.h>
#include <math.h>

int main()
{
    double a,b,c;
    int tag = 0;
    while ( scanf("%lf%lf%lf", &a,&b,&c) )
    {
        if ( a == 0 && b == 0 && c == 0 )
        {
            break;
        }   
        if ( a*b*c>0 )
        {
            printf( "Triangle #%d\nImpossible.\n\n", ++tag );
        }   
        else if ( a == -1 )
        {
            if ( b>=c )
            {
                printf( "Triangle #%d\nImpossible.\n\n", ++tag );
            }   
            else
            {
                printf( "Triangle #%d\na = %.3lf\n\n", ++tag, sqrt( c*c-b*b ) );
            }   
        }   
        else if ( b == -1 )
        {
            if ( a>=c )
            {
                printf( "Triangle #%d\nImpossible.\n\n", ++tag );
            }   
            else
            {
                printf( "Triangle #%d\nb = %.3lf\n\n", ++tag, sqrt( c*c-a*a ) );
            }   
        }  
        else if ( c == -1 )
        {
                printf( "Triangle #%d\nc = %.3lf\n\n", ++tag, sqrt( a*a+b*b ) );
        }    
       
    }   
   
    system( "PAUSE" );
    return 0;
}    