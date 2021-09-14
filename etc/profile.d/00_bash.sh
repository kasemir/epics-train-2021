alias ll="ls -lh"
alias la="ls -lah"
alias ..="cd .."

# Remove the long host name from prompt
if [ `hostname` = "training-VirtualBox" ]
then
    export PS1="\[\e]0;\u@VB: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@VB\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ "
fi


