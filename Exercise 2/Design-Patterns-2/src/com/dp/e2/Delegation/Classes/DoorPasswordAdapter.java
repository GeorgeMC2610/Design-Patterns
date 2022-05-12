package com.dp.e2.Delegation.Classes;

public class DoorPasswordAdapter implements PasswordClient
{
    @Override
    public void alarm()
    {
        System.out.println("ioy ioy");
    }
}
