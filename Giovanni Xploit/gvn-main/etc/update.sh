#!/bin/bash

#            ---------------------------------------------------
#                         Giovanni Android Framework                                                  
#            ---------------------------------------------------
#                           johnmadaha6@gmail.com

#blue start 
	BS="-e \033[1;34m"
#color end
	CE="\033[0m"
#red start
	RS="\033[0;31m"
	C="\033[0m"
#green start
	GN="\033[0;32m"
#white start
        WHS="\033[0m"

if [[ -d /data/data/com.termux ]]
then
if [[ -f /data/data/com.termux/files/usr/bin/gvn ]]
then
UPD="true"
else
UPD="false"
fi
else
if [[ -f /usr/local/bin/gvn ]]
then
UPD="true"
else
UPD="false"
fi
fi
{
ASESR="$( curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//' )"
} &> /dev/null
if [[ "$ASESR" = "" ]]
then 
sleep 1
echo -e ""$GN"["$RS"+"$GN"]"$CE" Download failed!"$C""
sleep 1
exit
fi
if [[ $EUID -ne 0 ]]
then
sleep 1
echo -e ""$GN"["$RS"+"$GN"]"$CE" Permission denied!"$C""
sleep 1
exit
fi
sleep 1
echo -e ""$GN"["$RS"+"$GN"]"$CE" Installing update..."$C""
{
rm -rf ~/gvn
rm /bin/gvn
rm /usr/local/bin/gvn
rm /data/data/com.termux/files/usr/bin/gvn
cd ~
git clone https://github.com/GiovanniJohnArthur/Ghost-Xploit
if [[ "$UPD" != "true" ]]
then
sleep 0
else
cd ghost
chmod +x install.sh
./install.sh
fi
} &> /dev/null
echo -e ""$GN"["$RS"+"$GN"]"$CE" Successfully updated!"$C""
cd .
touch .updated
sleep 1
exit
