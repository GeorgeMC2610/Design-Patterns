package com.dp.e2.Delegation.Classes;

public class PasswordProtector
{
    private int safeNumber;
    private PasswordClient passwordClient;

    public PasswordProtector()
    {
        this.safeNumber = -1;
        this.passwordClient = null;
    }

    public void Register(int safeNumber, PasswordClient passwordClient)
    {
        this.safeNumber = safeNumber;
        this.passwordClient = passwordClient;
        this.passwordClient.setPasswordProtector(this);
    }

    public void Check(int code)
    {
        if (this.safeNumber == -1)
            System.out.println("You must register first.");
        else if (code != this.safeNumber)
            passwordClient.alarm();
        else
            System.out.println("Successful entry.");
    }
}
