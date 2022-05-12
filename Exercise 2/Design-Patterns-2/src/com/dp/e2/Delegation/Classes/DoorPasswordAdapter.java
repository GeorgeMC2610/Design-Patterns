package com.dp.e2.Delegation.Classes;

public class DoorPasswordAdapter extends PasswordClient
{
    private ProtectedDoor protectedDoor;

    public DoorPasswordAdapter(ProtectedDoor protectedDoor)
    {
        this.protectedDoor = protectedDoor;
    }

    @Override
    public void alarm()
    {
        protectedDoor.alarm();
    }

    public void check(int number)
    {
        //since this class derives the password protector from its superclass, it can be called
        passwordProtector.Check(number);
    }
}
