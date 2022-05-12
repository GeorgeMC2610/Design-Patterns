package com.dp.e2.Delegation.Classes;

public class ProtectedDoor extends Door
{
    private DoorPasswordAdapter theDoorPasswordAdapter;

    public void alarm()
    {
        theDoorPasswordAdapter.alarm();
    }
}
