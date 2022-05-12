package com.dp.e2.MultipleInheritance.Classes;

public abstract class PasswordClient
{
    private PasswordProtector passwordProtector;
    public void SetPasswordProtector(PasswordProtector passwordProtector)
    {
        this.passwordProtector = passwordProtector;
    }

    public abstract void alarm();
}
