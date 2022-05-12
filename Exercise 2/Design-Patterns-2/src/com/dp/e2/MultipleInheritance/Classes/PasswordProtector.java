package com.dp.e2.MultipleInheritance.Classes;


public class PasswordProtector
{
    private int safeNumber;
    private PasswordClient passwordClient;

    public PasswordProtector()
    {
        this.safeNumber = -1;
    }

    public void Register(int safeNumber, PasswordClient passwordClient)
    {
        this.safeNumber = safeNumber;
        this.passwordClient = passwordClient;
        this.passwordClient.SetPasswordProtector(this);
    }

    public void Check(int code)
    {
        if (code != safeNumber)
            passwordClient.alarm();

        else
            System.out.println("Success.");
    }
}
