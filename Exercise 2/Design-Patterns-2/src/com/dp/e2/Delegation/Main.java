package com.dp.e2.Delegation;

import com.dp.e2.Delegation.Classes.*;

public class Main
{

    public static void main(String... args)
    {
        // === ΓΕΩΡΓΙΟΣ ΣΕΪΜΕΝΗΣ - Π19204 ===
        // 2η Εργασία στα Πρότυπα Ανάπτυξης Λογισμικού
        // Υλοποίηση ISP μέσω Αποστολής Μηνυμάτων.
        System.out.println("=== DELEGATION ===\n\n");

        PasswordProtector p1 = new PasswordProtector();
        ProtectedDoor protectedDoor = new ProtectedDoor();

        p1.Register(987190, protectedDoor.getDoorPasswordAdapter());
        protectedDoor.lock();
        protectedDoor.unlock();
    }
}
