package com.dp.e2.Delegation.Classes;

public abstract class PasswordClient
{
    private PasswordProtector passwordProtector;
    public void setPasswordProtector(PasswordProtector passwordProtector)
    {
        this.passwordProtector = passwordProtector;
    }

    public abstract void alarm();

}
