<?php

print("<meta charset=\"UTF-8\">");
print("<body>");

$myuid = $_GET['uid'];
if ($myuid == "") $myuid = $_POST['uid'];
if ($myuid == "") {
$myuid = md5($_SERVER['REMOTE_ADDR']).date("Y-m-d_H-i-s");
while (file_exists($myuid.".csv")) {
$myuid = $myuid."1";
}
$myuid = $myuid.".csv";
}

$nextpage = "";
$csv = "";
foreach( $_POST as $k => $stuff ) {
    if ($k == "uid" && $stuff != "") $myuid=$stuff;
    if ($k == "page" && $stuff == "0") $nextpage="-1";
    if ($k == "page" && $stuff == "1") $nextpage="-2";
    if ($k == "page" && $stuff == "2") $nextpage="-3";
    if ($k != "page" && $k != "uid") {
    $csv = $csv.$k.",";
    if( is_array( $stuff ) ) {
        foreach( $stuff as $ke => $thing ) {
            if ($ke>0) $csv .= ",";
            $csv = $csv.str_replace(",", ";", $thing);
        }
    } else {
        $csv = $csv.$stuff;
    }
    $csv = $csv."\n";
    }
}

//print($csv);
print("Sto salvando le tue risposte");
$old = "";
if ($nextpage == "-1") {
$old = "Domanda,Risposte\n";
} else {
$old = file_get_contents($myuid);
}
$csv = $old.$csv;
file_put_contents($myuid, $csv);

if ($nextpage!="") print("<meta http-equiv=refresh content=\"0; url=questionario-informaggio".$nextpage.".html?uid=".$myuid."\">");

print("</body>");

?>
