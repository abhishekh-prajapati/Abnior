$targetPath = "C:\Users\Abhishekh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ABNIOR.lnk"
$sourcePath = "python.exe"
$arguments = "p:\Abnior\main.py"
$workingDirectory = "p:\Abnior"

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($targetPath)
$Shortcut.TargetPath = $sourcePath
$Shortcut.Arguments = $arguments
$Shortcut.WorkingDirectory = $workingDirectory
$Shortcut.Save()

Write-Host "ABNIOR added to Windows Startup. It will launch next time you log in."
