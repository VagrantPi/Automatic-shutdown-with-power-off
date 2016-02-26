# Automatic-shutdown-with-power-off

使用兩顆行動電源分別供應小Pi電源（前面有版本是單顆的）

並於固定時間ping路由器，當ping不到時自動關機

用GPIO17控制記電器，來幫電池

用GPIO18控制開關切換供給小Pi的行動電源

使用前先創四個記錄檔

    echo "0" > PowerOnTime
    echo "0" > PowerOffTime
    echo "0" > PowerOnTime2
    echo "0" > PowerOffTime2


請把程式放到背景直行，可按Ctrl + Z 或

    sudo python UPS.py &

