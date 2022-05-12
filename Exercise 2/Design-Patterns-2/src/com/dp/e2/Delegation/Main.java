package com.dp.e2.Delegation;

import com.dp.e2.Delegation.Classes.*;

public class Main {

    public static void main(String[] args)
    {
        PasswordProtector p1 = new PasswordProtector();
        ProtectedDoor protectedDoor = new ProtectedDoor();

        p1.Register(987190, protectedDoor.getDoorPasswordAdapter());
        protectedDoor.lock();
        protectedDoor.unlock();
    }
}
