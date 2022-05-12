package com.dp.e2.Delegation.Classes;

import java.util.Scanner;

public class ProtectedDoor implements Door
{
    private DoorPasswordAdapter doorPasswordAdapter;

    public ProtectedDoor()
    {
        doorPasswordAdapter = new DoorPasswordAdapter(this);
    }

    public void alarm()
    {
        System.out.println("ALARM: Wrong password!");
    }

    @Override
    public void lock()
    {
        int passcode;
        Scanner scanner = new Scanner(System.in);

        System.out.print("To lock, enter your password: ");
        passcode = scanner.nextInt();

        doorPasswordAdapter.check(passcode);
    }

    @Override
    public void unlock()
    {
        int passcode;
        Scanner scanner = new Scanner(System.in);

        System.out.print("To unlock, enter your password: ");
        passcode = scanner.nextInt();

        doorPasswordAdapter.check(passcode);
    }

    public DoorPasswordAdapter getDoorPasswordAdapter()
    {
        return this.doorPasswordAdapter;
    }
}
