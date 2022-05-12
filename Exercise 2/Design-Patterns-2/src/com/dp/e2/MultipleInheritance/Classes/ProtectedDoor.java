package com.dp.e2.MultipleInheritance.Classes;

import java.util.Scanner;

public class ProtectedDoor extends PasswordClient implements Door
{
    public ProtectedDoor(PasswordProtector passwordProtector)
    {
        this.passwordProtector = passwordProtector;
    }

    PasswordProtector passwordProtector;

    @Override
    public void alarm()
    {
        System.out.println("WRONG PASSWORD.");
    }

    @Override
    public void lock()
    {
        int passcode;
        Scanner scanner = new Scanner(System.in);

        System.out.print("To lock your door, enter your password: ");
        passcode = scanner.nextInt();

        passwordProtector.Check(passcode);
    }

    @Override
    public void unlock()
    {
        int passcode;
        Scanner scanner = new Scanner(System.in);

        System.out.print("To unlock your door, enter your password: ");
        passcode = scanner.nextInt();

        passwordProtector.Check(passcode);

    }
}
