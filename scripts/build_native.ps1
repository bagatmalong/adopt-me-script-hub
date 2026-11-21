param([string]$Configuration = "Release")
dotnet build ./native/executor_bridge/ExecutorBridge.csproj -c $Configuration
Write-Host "native bridge built -> native/executor_bridge/bin/$Configuration"