package com.dp.e2.MultipleInheritance;
import com.dp.e2.MultipleInheritance.Classes.*;

public class Main
{
    public static void main(String... args)
    {
        PasswordProtector protector = new PasswordProtector();
        ProtectedDoor door = new ProtectedDoor(protector);
        protector.Register(298747, door);

        door.lock();
        door.unlock();
    }
}
