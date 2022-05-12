package com.dp.e1.shapes;

public class Shape
{
    private int xUpperLeftCorner;
    private int yUpperLeftCorner;

    private int width;
    private int height;

    public Shape(int xUpperLeftCorner, int yUpperLeftCorner, int width, int height)
    {
        this.xUpperLeftCorner = xUpperLeftCorner;
        this.yUpperLeftCorner = yUpperLeftCorner;
        this.width = width;
        this.height = height;
    }

    public void draw()
    {
        System.out.println("Drawing shape with dimensions " + String.valueOf(width) + "⨯" + String.valueOf(height) + ".");
    }

    //LCOM
    // 1 - (1+1+2+2)/2*4 = 1 - 6/8 = 8/8 - 6/8 = 2/8 = 0.25
}
