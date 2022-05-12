package com.dp.e2.Delegation.Classes;

public class ProtectedDoor implements Door
{
    private DoorPasswordAdapter doorPasswordAdapter;
    private PasswordProtector passwordProtector;

    public void alarm()
    {
        doorPasswordAdapter.alarm();
    }

    @Override
    public void lock()
    {

    }

    @Override
    public void unlock()
    {

    }
}
