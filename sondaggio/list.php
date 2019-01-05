<?php
if ($handle = opendir('.')) {
    $zip = new ZipArchive;
    $zipname = 'latest_informaggio_csv.zip';
    $dozip = 0;
    if ($zip->open($zipname, ZipArchive::OVERWRITE) === TRUE) $dozip = 1;
    while (false !== ($entry = readdir($handle))) {

        if ($entry != "." && $entry != ".." && substr($entry, -4)==".csv") {
            echo "<a href =\"".$entry."\">".$entry."</a></br>";
            if ($dozip==1) $zip->addFile($entry);
        }
    }
    if ($dozip==1) $zip->close();
    closedir($handle);
}
if ($dozip==1) echo "</br></br>ZIP completo: <a href =\"".$zipname."\">".$zipname."</a></br>";
?>
