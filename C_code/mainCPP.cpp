    #include<stdio.h>
    #include<stdint.h>

    void add(int &a,int &b)
    {
        a = a + 20;
        b = b + 20;
        printf("inside add\n");
        printf("a - %d\nb - %d",a,b);
    }

    int main()
    {
        int a=10,b=20;
        add(a,b);
        printf("\noutside add\n");
        printf("a - %d\nb - %d\n",a,b);
        return 0;
    }