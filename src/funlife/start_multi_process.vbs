Dim i
i = 5
while i > 0
	Dim WinScriptHost
	Set WinScriptHost = CreateObject("WScript.shell")
	WinScriptHost.Run Chr(34) & ".\start.bat" & Chr(34), 1
	Set WinScriptHost = Nothing
	i = i - 1
Wend