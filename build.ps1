$exclude = @("venv", "bot_pdf.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_pdf.zip" -Force