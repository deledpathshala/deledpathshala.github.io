# Generate pdf-index.json from assets/pdfs/*
$base = Join-Path (Get-Location).Path "assets\pdfs"

if (-not (Test-Path -LiteralPath $base)) {
  Write-Host "ERROR: Folder not found: $base"
  Write-Host "Check: assets\pdfs\sem1 ... exists in your repo."
  exit 1
}

$items =
  Get-ChildItem -Path $base -Recurse -Filter *.pdf -File |
  ForEach-Object {
    $full = $_.FullName
    $rel  = $full.Substring($base.Length).TrimStart("\","/")   # sem1\file.pdf
    $parts = $rel -split "[\\/]"                               # ["sem1","file.pdf"]
    $sem = $parts[0]
    $fileName = $parts[-1]

    $title = [System.IO.Path]::GetFileNameWithoutExtension($fileName)
    $title = ($title -replace "_"," " -replace "\s+"," ").Trim()

    # URL-encode filename (spaces, (), Hindi etc.)
    $encodedFile = [Uri]::EscapeDataString($fileName)
    $url = "./assets/pdfs/$sem/$encodedFile"

    $type = "PDF"
    if ($title -match "(?i)\bpyq\b|solved paper|previous year|हल|प्रश्नपत्र") { $type = "PYQ" }
    elseif ($title -match "(?i)internship|इंटर्नशिप") { $type = "Internship" }
    elseif ($title -match "(?i)important|important questions") { $type = "Important" }
    elseif ($title -match "(?i)notes") { $type = "Notes" }

    [PSCustomObject]@{
      semester = $sem
      title   = $title
      type    = $type
      sizeMB  = [Math]::Round(($_.Length/1MB), 1)
      url     = $url
    }
  } |
  Sort-Object semester, title

$items | ConvertTo-Json -Depth 4 | Set-Content -Path ".\pdf-index.json" -Encoding UTF8

Write-Host "DONE: pdf-index.json generated in repo root."