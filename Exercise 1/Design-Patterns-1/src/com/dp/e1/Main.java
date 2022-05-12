package com.dp.e1;
import com.dp.e1.modem.*;
import com.dp.e1.shapes.*;

public class Main
{
    public static void main(String[] args)
    {
        System.out.println("--- Π19204, ΓΕΩΡΓΙΟΣ ΣΕΪΜΕΝΗΣ ---");
        System.out.println("Πρότυπα ανάπτυξης λογισμικού - Προαιρετική 1");
        System.out.println("Ακολουθεί ένα παράδειγμα για κάθε κλάση.");
        System.out.println("");

        Shape shape1 = new Shape(520, 429, 1920, 1080);
        GeometricShape geometricShape1 = new GeometricShape(shape1, 220, 159);

        shape1.draw();

        ModemImplementation modem1 = new ModemImplementation("2106545087",
                "DESKTOP-JF109LK",
                "DESKTOP-AJ209TR",
                "LAPTOP-KK628AZ");

        modem1.dial("2104492822");
        modem1.hangup();

        ModemImplementation modem2 = new ModemImplementation("2106545887");

        modem1.DisplayDevices();
        modem2.DisplayDevices();
    }
}
