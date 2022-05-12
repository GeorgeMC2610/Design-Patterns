package com.company.modem;

public class ModemImplementation implements Connection, DataChannel
{

    //Connection
    @Override
    public char recv()
    {
        return 'r';
    }

    @Override
    public void send(char c)
    {
        System.out.println("Sending " + c + "...");
    }

    //DataChannel
    @Override
    public void dial()
    {
        System.out.println("Dialing...");
    }

    @Override
    public void hangup()
    {
        System.out.printf("Hanging up...");
    }
}
