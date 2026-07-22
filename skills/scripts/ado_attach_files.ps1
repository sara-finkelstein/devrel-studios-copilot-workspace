<#
.SYNOPSIS
    Attach one or more local files to an Azure DevOps work item.

.DESCRIPTION
    The Azure DevOps MCP server only exposes attachment *download*, not upload,
    so this script talks to the ADO REST API directly using an Azure CLI
    access token (no PAT needed if you're already `az login`'d with access to
    the org).

    For each file: uploads the content to the Attachments API, then PATCHes
    the work item to add an AttachedFile relation pointing at it.

.PARAMETER Organization
    Azure DevOps organization name, e.g. "devrel".

.PARAMETER Project
    Azure DevOps project name, e.g. "Studios".

.PARAMETER WorkItemId
    The numeric work item ID to attach files to.

.PARAMETER Files
    One or more local file paths to attach.

.EXAMPLE
    .\ado_attach_files.ps1 -Organization devrel -Project Studios -WorkItemId 228786 `
        -Files "C:\Downloads\ep.srt","C:\Downloads\ep.vtt","C:\Downloads\ep.ttml"
#>
param(
    [Parameter(Mandatory = $true)][string]$Organization,
    [Parameter(Mandatory = $true)][string]$Project,
    [Parameter(Mandatory = $true)][int]$WorkItemId,
    [Parameter(Mandatory = $true)][string[]]$Files
)

$ErrorActionPreference = "Stop"

# Azure DevOps resource ID (fixed, well-known GUID) for token scoping.
$resource = "499b84ac-1321-427f-aa17-267ca6975798"
$token = az account get-access-token --resource $resource --query accessToken -o tsv
if (-not $token) {
    throw "Failed to get an Azure DevOps access token. Run 'az login' first."
}
$headers = @{ Authorization = "Bearer $token" }

$attached = @()
foreach ($file in $Files) {
    if (-not (Test-Path $file)) {
        Write-Warning "Skipping missing file: $file"
        continue
    }
    $fileName = Split-Path $file -Leaf

    # Step 1: upload the file content to the Attachments API.
    $uploadUrl = "https://dev.azure.com/$Organization/$Project/_apis/wit/attachments?fileName=$([uri]::EscapeDataString($fileName))&api-version=7.1"
    $bytes = [System.IO.File]::ReadAllBytes($file)
    $uploadResp = Invoke-RestMethod -Uri $uploadUrl -Method Post -Headers $headers -Body $bytes -ContentType "application/octet-stream"
    $attachmentUrl = $uploadResp.url
    Write-Host "Uploaded $fileName -> $attachmentUrl"

    # Step 2: PATCH the work item to add the AttachedFile relation.
    $patchUrl = "https://dev.azure.com/$Organization/$Project/_apis/wit/workitems/$($WorkItemId)?api-version=7.1"
    $patchBody = @(
        @{
            op    = "add"
            path  = "/relations/-"
            value = @{
                rel        = "AttachedFile"
                url        = $attachmentUrl
                attributes = @{ comment = "Added via Copilot CLI frameio-transcript-pipeline skill" }
            }
        }
    ) | ConvertTo-Json -Depth 5 -AsArray

    $patchHeaders = $headers.Clone()
    Invoke-RestMethod -Uri $patchUrl -Method Patch -Headers $patchHeaders -Body $patchBody -ContentType "application/json-patch+json" | Out-Null
    Write-Host "Linked $fileName to work item $WorkItemId"
    $attached += $fileName
}

Write-Host ""
Write-Host "Done. Attached $($attached.Count) file(s) to https://dev.azure.com/$Organization/$Project/_workitems/edit/$WorkItemId"
