using System.Diagnostics;

namespace AdoptMe.ExecutorBridge;

/// <summary>Minimal helper used by the Python host to locate the Roblox client.</summary>
public static class AttachHelper
{
    public static int? FindRobloxPid()
    {
        foreach (var p in Process.GetProcessesByName("RobloxPlayerBeta"))
        {
            return p.Id;
        }
        return null;
    }

    public static bool IsAlive(int pid)
    {
        try { return !Process.GetProcessById(pid).HasExited; }
        catch { return false; }
    }
}