# /ics/etc/setup.sh,
# link into /etc/profile.d
#
#     sudo ln -s /ics/etc/setup.sh /etc/profile.d/ics.sh
#
# Sources all files in ics/etc/profile.d
# in alphabetical order

for i in /ics/etc/profile.d/*.sh
do
    . "$i"
done

