package com.dp.e2.Delegation.Classes;

public abstract class PasswordClient
{
    protected PasswordProtector passwordProtector;
    public void setPasswordProtector(PasswordProtector passwordProtector)
    {
        this.passwordProtector = passwordProtector;
    }

    //this is implemented in ProtectedDoor
    public abstract void alarm();
}
