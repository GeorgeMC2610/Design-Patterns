package com.dp.e1.modem;

public class ModemImplementation implements Connection, DataChannel
{
    private String OwnNumber;
    private String DialedNumber;
    private String[] ConnectedDevices;

    public ModemImplementation(String OwnNumber)
    {
        this.OwnNumber = OwnNumber;
    }

    public ModemImplementation(String OwnNumber, String... ConnectedDevices)
    {
        this.OwnNumber = OwnNumber;
        this.ConnectedDevices = ConnectedDevices;
    }

    //from DataChannel
    @Override
    public void hangup()
    {
        //if the dialed number is null then there's no reason to hung up.
        if (this.DialedNumber == null)
        {
            System.out.println("Line is not in use.");
            return;
        }

        System.out.println("Hung up " + this.DialedNumber + ".");
        this.DialedNumber = null;
    }

    @Override
    public void dial(String pno)
    {
        //if the pno is not null, it means that the line is busy.
        if (this.DialedNumber != null)
        {
            System.out.println("Line busy.");
            return;
        }

        //the pno must be a different number than ownnumber.
        if (pno.equals(this.OwnNumber))
        {
            System.out.println("Phone number is the same.");
            return;
        }

        System.out.println("Dialing to " + pno + "...");
        this.DialedNumber = pno;
    }

    //from Connection
    @Override
    public char recv()
    {
        if (this.DialedNumber == null)
        {
            System.out.println("Line is not in use. Cannot receive.");
            return 1;
        }

        return 0;
    }

    @Override
    public void send(char c)
    {
        if (this.DialedNumber == null)
        {
            System.out.println("The line is not in use, cannot send.");
            return;
        }

        System.out.println("Sending signal to " + this.DialedNumber + "...");
    }

    public void DisplayDevices()
    {
        if (ConnectedDevices == null || ConnectedDevices.length == 0)
        {
            System.out.println("No devices connected.");
            return;
        }

        for (int i = 0; i < ConnectedDevices.length; i++)
            System.out.println("DEVICE " + String.valueOf(i + 1) + ": " + ConnectedDevices[i]);
    }

    //getters
    public String getOwnNumber()
    {
        return this.OwnNumber;
    }

    public String[] getConnectedDevices()
    {
        return this.ConnectedDevices;
    }

    //setters
    public void setConnectedDevices(String... ConnectedDevices)
    {
        this.ConnectedDevices = ConnectedDevices;
    }

    //LCOM
    // 1 - (sum(methods reference for each field) / method count * field count))
    // 1 - (sum(4,4,4)/3*10) 18/30) = 0.6
}
