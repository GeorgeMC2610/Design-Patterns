package com.dp.e1.shapes;

public class GeometricShape
{
    private Shape shape;
    private int xLowerRightCorner;
    private int yLowerRightCorner;

    public GeometricShape(Shape shape, int xLowerRightCorner, int yLowerRightCorner)
    {
        this.shape = shape;
        this.xLowerRightCorner = xLowerRightCorner;
        this.yLowerRightCorner = yLowerRightCorner;
    }

    public int getXLowerRightCorner()
    {
        return xLowerRightCorner;
    }

    public int getYLowerRightCorner()
    {
        return yLowerRightCorner;
    }

    //LCOM
    // 1 - (sum(methods reference for each field) / method count * field count))
    // 1 - (1+2+2)/3*3 = 1 - 5/9 = 0.44
}
