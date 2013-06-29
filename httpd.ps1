param($Root=".", $Port=8080, $HostName="localhost")

pushd $Root
$Root = pwd

$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://$HostName`:$Port/")
$listener.Start()

echo ("Start {0} at `"$Root`"" -f ($listener.Prefixes | select -f 1))
echo "Enter Ctrl + C to stop."

while ($true) {
    $context = $listener.GetContext()

    $url = $context.Request.Url.LocalPath.TrimStart('/')
    $res = $context.Response
    $path = Join-Path $Root ($url -replace "/","\")
    echo $path

    if ((Test-Path $path -PathType Leaf) -eq $true) {
        $content = [IO.File]::ReadAllBytes($path)
        $res.OutputStream.Write($content, 0, $content.Length)
    }
    else {
        $res.StatusCode = 404
    }
    $res.Close()
}

