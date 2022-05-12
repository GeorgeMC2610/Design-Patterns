package com.dp.e2.MultipleInheritance;
import com.dp.e2.MultipleInheritance.Classes.*;

public class Main
{
    public static void main(String... args)
    {
        // === ΓΕΩΡΓΙΟΣ ΣΕΪΜΕΝΗΣ - Π19204 ===
        // 2η Εργασία στα Πρότυπα Ανάπτυξης Λογισμικού
        // Υλοποίηση ISP μέσω Πολλαπλής Κληρονομικότητας.

        PasswordProtector protector = new PasswordProtector();
        ProtectedDoor door = new ProtectedDoor(protector);
        protector.Register(298747, door);

        door.lock();
        door.unlock();
    }
}
